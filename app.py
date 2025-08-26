from flask import Flask, render_template, request, redirect, url_for, flash
from sqlite3 import Connection, Cursor, connect


app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"

books: list[dict[str, str]] = [
    {
        "author_name": "Samuel P. Huntington",
        "book_name": "The Clash of Civilizations and the Remaking of World Order",
        "reader_description": "Not a bad book, but a shallow book about most of the things."
    },
    {
        "author_name": "Graham Greene",
        "book_name": "Our Man in Havana",
        "reader_description": "A witty and satirical spy novel, light but insightful."
    },
    {
        "author_name": "George Orwell",
        "book_name": "1984",
        "reader_description": "A dark dystopian vision of the future, still relevant today."
    },
    {
        "author_name": "Daniel",
        "book_name": "The book Of Daniel",
        "reader_description": "A revolutionary book and surrealistic."
    }
]

@app.route("/", methods=["GET", "POST"])
def index(): # I might need to separate this function
    if request.method == "POST":
        title: str = (request.form.get("book_input") or "").strip()
        author: str = (request.form.get("author_input") or "").strip()
        description: str = (request.form.get("description_input") or "").strip()

        if not title or not author or not description:
            flash("Please fill in all fields.", "error")
        else:
            books.append({
                "author_name": author,
                "book_name": title,
                "reader_description": description
            })
            flash(f'Your book "{title}" has been added!', 'success')
        return redirect(url_for("index"))
    # book_list is reverse here because I want get 3 recent item in the list in the html.
    return render_template("index.html", book_list=books[::-1])


# This function will add data to the book.db
def add_book_to_db(book: dict[str, str]) -> None:
    conn: Connection = connect("book.db")
    cursor: Cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_name TEXT NOT NULL,
            book_name TEXT NOT NULL,
            reader_description TEXT NOT NULL
        )
    """)
    cursor.execute("""
        INSERT INTO books (author_name, book_name, reader_description)
        VALUES (?, ?, ?)
    """, (book["author_name"], book["book_name"], book["reader_description"]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
