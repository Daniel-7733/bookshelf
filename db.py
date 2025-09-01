from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy() # create the db object here


# engine = create_engine("sqlite:///instance/book.db")

# # This function will add data to the book.db
# def add_book_to_db(book: dict[str, str]) -> None:
#     conn: Connection = connect("book.db")
#     cursor: Cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             author_name TEXT NOT NULL,
#             book_name TEXT NOT NULL,
#             reader_description TEXT NOT NULL
#         )
#     """)
#     cursor.execute("""
#         INSERT INTO books (author_name, book_name, reader_description)
#         VALUES (?, ?, ?)
#     """, (book["author_name"], book["book_name"], book["reader_description"]))
#     conn.commit()
#     conn.close()