from flask import Flask, render_template, request, redirect, url_for, flash

app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret"

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
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = (request.form.get("book_input") or "").strip()
        if not title:
            flash("Please enter a book title.", "error")
        else:
            books.append({
                "author_name": "Unknown",
                "book_name": title,
                "reader_description": "No description yet."
            })
            flash(f"Your book '{title}' has been added!", "success")
        return redirect(url_for("index"))

    return render_template("index.html", book_list=books)

if __name__ == "__main__":
    app.run(debug=True)
