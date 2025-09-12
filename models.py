from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from db import db



class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(200), unique=True, nullable=False, index=True)
    password_hash: str = db.Column(db.String(256), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # one-to-many: a user has many books
    books = db.relationship(
        "Book",
        back_populates="owner",
        cascade="all, delete-orphan",
        passive_deletes=True,
        lazy="dynamic",   # allows .filter(), .count() on current_user.books
    )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User {self.id} {self.email}>"



class Book(db.Model):
    __tablename__ = "books"

    id: int = db.Column(db.Integer, primary_key=True)
    author_name: str = db.Column(db.String(100), nullable=False)
    book_name: str = db.Column(db.String(200), nullable=False, index=True)
    reader_description: str = db.Column(db.Text, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # FK to users.id
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # relationship back to User
    owner = db.relationship("User", back_populates="books")

    def __repr__(self) -> str:
        return f"<Book {self.book_name} by {self.author_name} (user={self.user_id})>"



# ----------------- old model which work without user ------------------------------#
# from werkzeug.security import generate_password_hash, check_password_hash
# from db import db
#
#
# class Book(db.Model):
#     id: int = db.Column(db.Integer, primary_key=True)
#     author_name: str = db.Column(db.String(100), nullable=False)
#     book_name: str = db.Column(db.String(200), nullable=False)
#     reader_description: str = db.Column(db.Text, nullable=False)
#
#     def __repr__(self) -> str:
#         return f"<Book {self.book_name} by {self.author_name}>"
#
#
# class User(db.Model):
#     id: int = db.Column(db.Integer, primary_key=True)
#     email: str = db.Column(db.String(200), unique=True, nullable=False)
#     password_hash: str = db.Column(db.String(200), nullable=False)
#
#     def __repr__(self) -> str:
#         return f"<Email is {self.email} and password is {self.password}>"
#
#     def set_password(self, password: str) -> None:
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password: str) -> bool:
#         return check_password_hash(self.password_hash, password)