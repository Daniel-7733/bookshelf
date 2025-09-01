from db import db

# Making a class & the model
class Book(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    author_name: str = db.Column(db.String(100), nullable=False)
    book_name: str = db.Column(db.String(200), nullable=False)
    reader_description: str = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Book {self.book_name} by {self.author_name}>"


# books: list[dict[str, str]] = [
#     {
#         "author_name": "Samuel P. Huntington",
#         "book_name": "The Clash of Civilizations and the Remaking of World Order",
#         "reader_description": "Not a bad book, but a shallow book about most of the things."
#     },
#     {
#         "author_name": "Graham Greene",
#         "book_name": "Our Man in Havana",
#         "reader_description": "A witty and satirical spy novel, light but insightful."
#     },
#     {
#         "author_name": "George Orwell",
#         "book_name": "1984",
#         "reader_description": "A dark dystopian vision of the future, still relevant today."
#     },
#     {
#         "author_name": "Daniel",
#         "book_name": "The book Of Daniel",
#         "reader_description": "A revolutionary book and surrealistic."
#     }
# ]