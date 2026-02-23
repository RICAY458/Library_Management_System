from book_data import books
from utils import calculate_fine
from datetime import datetime, timedelta


def add_book(book_id, title):
    if book_id in books:
        return "Book ID already exists!"

    books[book_id] = {
        "title": title,
        "status": "Available",
        "borrower": None,
        "course": None,
        "section": None,
        "purpose": None,
        "date_borrow": None,
        "due_date": None,
        "date_return": None
    }
    return "Book added successfully!"


# Added course, section, and purpose parameters
def borrow_book(book_id, borrower, course, section, purpose):
    if book_id not in books:
        return "Invalid Book ID!"

    if books[book_id]["status"] == "Borrowed":
        return "Book is already borrowed."

    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=7)

    books[book_id].update({
        "status": "Borrowed",
        "borrower": borrower,
        "course": course,
        "section": section,
        "purpose": purpose,
        "date_borrow": borrow_date.strftime("%Y-%m-%d %H:%M"),
        "due_date": due_date,
        "date_return": "N/A"
    })

    return f"Book borrowed successfully! Due: {due_date.strftime('%Y-%m-%d')}"


def return_book(book_id):
    if book_id not in books:
        return "Invalid Book ID!"

    if books[book_id]["status"] == "Available":
        return "Book is not currently borrowed."

    fine = calculate_fine(books[book_id]["due_date"])

    # Record the return date before clearing
    books[book_id]["date_return"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    books[book_id]["status"] = "Available"
    books[book_id]["borrower"] = None
    # We keep the other data or clear it based on preference;
    # here we clear for the next borrower
    books[book_id]["due_date"] = None

    if fine > 0:
        return f"Book returned late! Fine: ₱{fine}"
    else:
        return "Book returned on time. No fine."


def view_books():
    return books