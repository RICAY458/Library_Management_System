import streamlit as st
import pandas as pd
from library import add_book, borrow_book, return_book, view_books
from book_data import books


# --- ULTIMATE AESTHETIC THEME ---
st.markdown("""
    <style>
    /* 1. Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. FORCE FORM LABELS TO WHITE */
    .stWidgetLabel p, label, .stMarkdown p {
        color: white !important;
        font-weight: 600 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    /* 3. Main Container - Frosted Glass */
    div.block-container {
        background: rgba(255, 255, 255, 0.1); 
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 3rem;
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-top: 2rem;
    }

    /* 4. Aesthetic Header Boxes */
    .aesthetic-header {
        background: linear-gradient(90deg, #2e3192 0%, #1bffff 100%);
        color: white !important;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }

    /* 5. BUTTON STYLING - BLACK TEXT */
    .stButton>button {
        background: linear-gradient(to right, #2e3192, #1bffff) !important;
        color: black !important; /* Changed word color to black */
        border-radius: 15px;
        font-weight: 800 !important; /* Extra bold for visibility */
        height: 3.5em;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(27, 255, 255, 0.4);
    }

    /* 6. Sidebar Styling */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(180deg, #2e3192 0%, #1bffff 100%) !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* 7. Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .metric-card h2 { color: #1bffff !important; font-size: 3rem; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Books Icon) ---
with st.sidebar:
    st.markdown("# 📚 LMS")
    st.write("Library Management System")
    st.divider()
    menu = st.radio("MAIN MENU", ["🏠 Dashboard", "➕ Add Book", "📖 Borrow Book", "🔄 Return Book", "📊 View Records"])

# ---------------- DASHBOARD ----------------
if menu == "🏠 Dashboard":
    st.markdown('<div class="aesthetic-header"><h1>📊 Dashboard Overview</h1></div>', unsafe_allow_html=True)
    total = len(books)
    borrowed = sum(1 for info in books.values() if info.get("status") == "Borrowed")
    available = total - borrowed

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="metric-card"><h3>TOTAL BOOKS</h3><h2>{total}</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><h3>BORROWED</h3><h2>{borrowed}</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><h3>AVAILABLE</h3><h2>{available}</h2></div>', unsafe_allow_html=True)

# ---------------- ADD BOOK ----------------
elif menu == "➕ Add Book":
    st.markdown('<div class="aesthetic-header"><h1>➕ Register New Item</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        book_id = st.text_input("Book ID")
    with col2:
        title = st.text_input("Book Title")
    if st.button("Add to Library"):  # This word is now BLACK
        if book_id and title:
            st.success(add_book(book_id, title))

# ---------------- BORROW BOOK ----------------
elif menu == "📖 Borrow Book":
    st.markdown('<div class="aesthetic-header"><h1>📖 Borrowing Portal</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        book_id = st.text_input("Book ID")
        borrower = st.text_input("Student Name")
        course = st.text_input("Course")
    with col2:
        section = st.text_input("Section")
        purpose = st.text_area("Purpose of Borrowing")
    if st.button("Confirm Transaction"):  # This word is now BLACK
        if all([book_id, borrower, course, section, purpose]):
            st.info(borrow_book(book_id, borrower, course, section, purpose))

# ---------------- RETURN BOOK ----------------
elif menu == "🔄 Return Book":
    st.markdown('<div class="aesthetic-header"><h1>🔄 Return Portal</h1></div>', unsafe_allow_html=True)
    book_id = st.text_input("Enter Book ID to Return")
    if st.button("Submit Return"):  # This word is now BLACK
        st.success(return_book(book_id))

# ---------------- VIEW RECORDS ----------------
elif menu == "📊 View Records":
    st.markdown('<div class="aesthetic-header"><h1>📊 Library Records Table</h1></div>', unsafe_allow_html=True)
    raw_data = view_books()
    if raw_data:
        table_data = [{"ID": k, **v} for k, v in raw_data.items()]
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:

        st.warning("Invalid Book ID. Please try again.")

