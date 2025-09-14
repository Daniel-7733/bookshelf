from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import Flask, render_template, request, flash, redirect, url_for, Response
from models import Book, User
from os import path, makedirs
from sqlalchemy import func
from db import db

app: Flask = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = "dev-secret"

makedirs(app.instance_path, exist_ok=True)
db_path: str = path.join(app.instance_path, "book.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# --- DB init ---
db.init_app(app)
with app.app_context():
    db.create_all()

# --- Flask-Login wiring ---
login_manager: LoginManager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "error"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ----------------------- Routes ----------------------- #

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            next_url = request.args.get("next")
            return redirect(next_url or url_for("home"))
        else:
            flash("Invalid email or password.", "error")

    return render_template("login.html")

# Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Signed out.", "success")
    return redirect(url_for("login"))

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        name: str = (request.form.get("name") or "").strip()
        username: str = (request.form.get("username") or "").strip()  # <-- REQUIRED by your model
        email: str = (request.form.get("email") or "").strip().lower()
        password: str = request.form.get("password") or ""

        if not name or not username or not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return redirect(url_for("register"))

        user: User = User(name=name, username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please sign in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# Home (gated) — show ONLY current user's books
@app.route("/home")
@login_required
def home() -> str:
    books: list[Book] = (
        Book.query.filter_by(user_id=current_user.id)
        .order_by(Book.id.desc())
        .limit(6)
        .all()
    )
    random_book: Book | None = (
        Book.query.filter_by(user_id=current_user.id)
        .order_by(func.random())
        .first()
    )
    return render_template("home.html", book_list=books, random_book=random_book)

# All books (gated) — only current user's books
@app.route("/books")
@login_required
def all_books() -> str:
    books: list[Book] = (
        Book.query.filter_by(user_id=current_user.id)
        .order_by(Book.id.desc())
        .all()
    )
    return render_template("all_books.html", book_list=books)

# Edit (gated + ownership check)
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id: int) -> Response | str:
    book: Book | None = Book.query.filter_by(id=book_id, user_id=current_user.id).first()
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for('all_books'))

    if request.method == 'POST':
        book.book_name = (request.form.get("book_name") or "").strip()
        book.author_name = (request.form.get("author_name") or "").strip()
        book.reader_description = (request.form.get("reader_description") or "").strip()
        db.session.commit()
        flash(f"Updated {book.book_name}", "success")
        return redirect(url_for('all_books'))

    return render_template('edit.html', book=book)

# Delete (gated + ownership check)
@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id: int) -> Response | str:
    book: Book | None = Book.query.filter_by(id=book_id, user_id=current_user.id).first()
    if not book:
        flash("Book not found.", "error")
        return redirect(url_for('all_books'))

    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash(f"Deleted {book.book_name}", "success")
        return redirect(url_for('all_books'))

    return render_template('delete.html', book=book)

# Add (gated) — attach to current_user
@app.route("/add", methods=["GET", "POST"])
@login_required
def add_book() -> Response | str:
    if request.method == "POST":
        title: str = (request.form.get("book_input") or "").strip()
        author: str = (request.form.get("author_input") or "").strip()
        description: str = (request.form.get("description_input") or "").strip()

        if not title or not author or not description:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("add_book"))

        new_book: Book = Book(
            author_name=author,
            book_name=title,
            reader_description=description,
            owner=current_user,   # <-- sets user_id
        )
        db.session.add(new_book)
        db.session.commit()
        flash(f'Book "{title}" has been added!', "success")
        return redirect(url_for("all_books"))

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
