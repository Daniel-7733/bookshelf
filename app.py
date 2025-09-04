from flask import Flask, render_template, request, flash, redirect, url_for
from models import Book
from db import db
import os


app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"
db_path = os.path.join(app.instance_path, "book.db") # I just make sure that my path does exist
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db with this app
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    books: list[Book] = Book.query.order_by(Book.id.desc()).all()
    return render_template("index.html", book_list=books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
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
