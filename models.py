from werkzeug.security import generate_password_hash, check_password_hash
from db import db


class Book(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    author_name: str = db.Column(db.String(100), nullable=False)
    book_name: str = db.Column(db.String(200), nullable=False)
    reader_description: str = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Book {self.book_name} by {self.author_name}>"


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(200), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"<Email is {self.email} and password is {self.password}>"

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
