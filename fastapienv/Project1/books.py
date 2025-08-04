"""
FastAPI Book Management API

This script demonstrates core FastAPI features:
- Path and query parameters
- Request body handling with Body()
- CRUD operations on an in-memory list
"""

from fastapi import Body, FastAPI

app = FastAPI()

# In-memory database of books
BOOKS = [
    {'title': 'Title one', 'author': 'Author One', 'category': 'Science Fiction'},
    {'title': 'Title seven', 'author': 'Author Seven', 'category': 'Science Fiction'},
    {'title': 'Title two', 'author': 'Author Two', 'category': 'Fantasy'},
    {'title': 'Title eight', 'author': 'Author Eight', 'category': 'Fantasy'},
    {'title': 'Title three', 'author': 'Author Three', 'category': 'Mystery'},
    {'title': 'Title four', 'author': 'Author Four', 'category': 'Non-Fiction'},
    {'title': 'Title five', 'author': 'Author Five', 'category': 'Biography'},
    {'title': 'Title six', 'author': 'Author Two', 'category': 'History'},
]


@app.get("/books")
async def read_all_books():
    """
    Retrieve all books.
    """
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    """
    Get a single book by its title (case-insensitive).
    """
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    """
    Get books filtered by category (query param).
    """
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return


@app.get("/books/{book_author}/")
async def read_author_by_category_by_query(book_author: str, category: str):
    """
    Get books by author and category using path and query param.
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
           book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    """
    Add a new book to the collection.
    """
    BOOKS.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    """
    Update an existing book using the title as the identifier.
    """
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    """
    Delete a book by title.
    """
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            deleted_book = BOOKS.pop(i)
            return {"message": "Book deleted successfully", "book": deleted_book}
    return {"message": "Book not found"}


@app.get("/books/by_author/{author}")
async def read_books_by_author_path(author: str):
    """
    Get all books by a specific author.
    """
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return
