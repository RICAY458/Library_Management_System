from book_data import books
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
        "date_return": None,
        "fine": "0.00",
        "note": "None"
    }
    return "Book added successfully!"

def borrow_book(book_id, borrower, course, section, purpose):
    if book_id not in books:
        return "Invalid Book ID!"

    if books[book_id]["status"] == "Borrowed":
        return "Book is already borrowed."

    # Use date only (no time) as requested
    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=7)

    books[book_id].update({
        "status": "Borrowed",
        "borrower": borrower,
        "course": course,
        "section": section,
        "purpose": purpose,
        # Formatted to YYYY-MM-DD
        "date_borrow": borrow_date.strftime("%Y-%m-%d"),
        "due_date": due_date.strftime("%Y-%m-%d"),
        "date_return": "N/A",
        "fine": "0.00",
        "note": "Borrowed"
    })

    return f"Book borrowed successfully! Due: {books[book_id]['due_date']}"

def return_book(book_id, return_date_str):
    if book_id not in books:
        return "Invalid Book ID!"

    if books[book_id]["status"] == "Available":
        return "Book is not currently borrowed."

    # Logic to identify if the return is on time or late
    due_date_obj = datetime.strptime(books[book_id]["due_date"], "%Y-%m-%d")
    return_date_obj = datetime.strptime(return_date_str, "%Y-%m-%d")

    # Calculate difference
    delay = (return_date_obj - due_date_obj).days

    if delay > 0:
        fine_amount = delay * 10.00 # Automatically calculates 10 pesos per day
        books[book_id]["fine"] = f"{fine_amount:.2f}"
        books[book_id]["note"] = f"Late by {delay} day(s)"
    else:
        books[book_id]["fine"] = "0.00"
        books[book_id]["note"] = "Returned on time"

    books[book_id]["date_return"] = return_date_str
    books[book_id]["status"] = "Available"
    books[book_id]["borrower"] = "None"

    if delay > 0:
        return f"Book returned late! Fine: ₱{books[book_id]['fine']}"
    else:
        return "Book returned on time. No fine."

def view_books():
    return books
