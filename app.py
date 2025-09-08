from flask import Flask, render_template, request, flash, redirect, url_for, Response
from models import Book
from db import db
import os


app: Flask = Flask(__name__, instance_relative_config=True) # 1) instance_relative_config=True lets us store book.db in ./instance
app.config["SECRET_KEY"] = "dev-secret"

os.makedirs(app.instance_path, exist_ok=True) # 2) Ensure the instance folder exists (important!)
db_path: str = os.path.join(app.instance_path, "book.db") # 3) Build an absolute path to instance/book.db (works on Windows)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db with this app
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index() -> str:
    books: list[Book] = Book.query.order_by(Book.id.desc()).all()
    return render_template("index.html", book_list=books)


@app.route("/books")
def all_books() -> str: # New route to display all books
    books: list[Book] = Book.query.order_by(Book.id.desc()).all()
    return render_template("all_books.html", book_list=books)


@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id: int) -> Response | str:
    book = Book.query.get_or_404(book_id)  # fetch by ID
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash(f"Deleted {book.book_name}", "success")
        return redirect(url_for('all_books'))
    return render_template('delete.html', book=book)



@app.route("/add", methods=["GET", "POST"])
def add_book() -> Response | str:
    if request.method == "POST":
        title: str = (request.form.get("book_input") or "").strip()
        author: str = (request.form.get("author_input") or "").strip()
        description: str = (request.form.get("description_input") or "").strip()

        if not title or not author or not description:
            flash("Please fill in all fields.", "error")
        else:
            new_book: Book = Book(
                author_name=author,
                book_name=title,
                reader_description=description
            )
            db.session.add(new_book)
            db.session.commit()
            flash(f'Book "{title}" has been added!', "success")

        return redirect(url_for("add_book"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
