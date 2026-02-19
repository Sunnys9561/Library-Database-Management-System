import mysql.connector
from datetime import datetime

# ------------------ DATABASE CONNECTION ------------------

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sunny",  # change this
        database="library_db"
    )

# ------------------ BOOK FUNCTIONS ------------------

def add_book():
    conn = connect_db()
    cursor = conn.cursor()

    title = input("Enter book title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    copies = int(input("Enter number of copies: "))

    query = """INSERT INTO books (title, author, category, total_copies, available_copies)
               VALUES (%s, %s, %s, %s, %s)"""
    values = (title, author, category, copies, copies)

    cursor.execute(query, values)
    conn.commit()
    print("Book added successfully!")

    conn.close()


def view_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n Book List:")
    for book in books:
        print(book)

    conn.close()


# ------------------ USER FUNCTIONS ------------------

def add_user():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter user name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, phone))
    conn.commit()

    print("User added successfully!")
    conn.close()


def view_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\n Users List:")
    for user in users:
        print(user)

    conn.close()


# ------------------ ISSUE BOOK ------------------

def issue_book():
    conn = connect_db()
    cursor = conn.cursor()

    book_id = int(input("Enter Book ID: "))
    user_id = int(input("Enter User ID: "))

    cursor.execute("SELECT available_copies FROM books WHERE book_id=%s", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        issue_date = datetime.today().date()

        cursor.execute("""INSERT INTO transactions 
                          (book_id, user_id, issue_date, status)
                          VALUES (%s, %s, %s, %s)""",
                       (book_id, user_id, issue_date, "Issued"))

        cursor.execute("""UPDATE books 
                          SET available_copies = available_copies - 1 
                          WHERE book_id=%s""", (book_id,))

        conn.commit()
        print("Book issued successfully!")
    else:
        print("Book not available!")

    conn.close()


# ------------------ RETURN BOOK ------------------

def return_book():
    conn = connect_db()
    cursor = conn.cursor()

    transaction_id = int(input("Enter Transaction ID: "))
    return_date = datetime.today().date()

    cursor.execute("""UPDATE transactions 
                      SET return_date=%s, status='Returned'
                      WHERE transaction_id=%s""",
                   (return_date, transaction_id))

    cursor.execute("""UPDATE books 
                      SET available_copies = available_copies + 1
                      WHERE book_id = (
                          SELECT book_id FROM transactions WHERE transaction_id=%s
                      )""", (transaction_id,))

    conn.commit()
    print("Book returned successfully!")

    conn.close()


# ------------------ REPORTS ------------------

def most_issued_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT book_id, COUNT(*) as issue_count
        FROM transactions
        GROUP BY book_id
        ORDER BY issue_count DESC
    """)

    results = cursor.fetchall()

    print("\n Most Issued Books:")
    for row in results:
        print(row)

    conn.close()


def overdue_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE status='Issued'
        AND issue_date < CURDATE() - INTERVAL 7 DAY
    """)

    results = cursor.fetchall()

    print("\n Overdue Books:")
    for row in results:
        print(row)

    conn.close()


# ------------------ MENU ------------------

def menu():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add User")
        print("4. View Users")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Most Issued Books Report")
        print("8. Overdue Books Report")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            view_users()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            most_issued_books()
        elif choice == "8":
            overdue_books()
        elif choice == "9":
            print("👋 Exiting...")
            break
        else:
            print(" Invalid choice!")

if __name__ == "__main__":
    menu()
