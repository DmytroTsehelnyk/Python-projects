from tabulate import tabulate
import sqlite3

db = sqlite3.connect("bookstore_db")
cursor = db.cursor()

# Create bookstore table
cursor.execute("""CREATE TABLE IF NOT EXISTS
                      bookstore(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)""")
# Commit the change
db.commit()


def show_in_table():
    """ Shows database information in user-friendly format"""

    # Initialize 2d list
    books_list = []

    for row in cursor:
        books_list.append([row[0], row[1], row[2], row[3]])

    bookshelf = tabulate(books_list, headers=["ID", "Title", "Author", "Quantity"], tablefmt="heavy_outline")
    print(bookshelf)


def find_last_id():
    """ Finds the last id in the database """

    cursor.execute('''SELECT id FROM bookstore''')
    last_id = 0
    for row in cursor:
        last_id = row[0]

    return last_id

# Initialize variables

ID_1 = 3001
ID_2 = 3002
ID_3 = 3003
ID_4 = 3004
ID_5 = 3005

Title_1 = "A Tale of Two Cities"
Title_2 = "Harry Potter and the Philosopher's Stone"
Title_3 = "The Lion, the Witch and the Wardrobe"
Title_4 = "The Lord of the Rings"
Title_5 = "Alice in Wonderland"

Author_1 = "Charles Dickens"
Author_2 = "J.K. Rowling"
Author_3 = "C.S. Lewis"
Author_4 = "J.R.R Tolkien"
Author_5 = "Lewis Carroll"

Qty_1 = 30
Qty_2 = 40
Qty_3 = 25
Qty_4 = 37
Qty_5 = 12

# Create list with tuples
books = [(ID_1, Title_1, Author_1, Qty_1),
         (ID_2, Title_2, Author_2, Qty_2),
         (ID_3, Title_3, Author_3, Qty_3),
         (ID_4, Title_4, Author_4, Qty_4),
         (ID_5, Title_5, Author_5, Qty_5)]

# Insert information into database
cursor.executemany('''INSERT OR IGNORE INTO bookstore(id, Title, Author, Qty) 
VALUES(?, ?, ?, ?)''', books)

# Commit the change
db.commit()


while True:
    menu = int(input("""Enter the number to choose an option below
1 - Add new book
2 - Update book 
3 - Delete book 
4 - Search books 
5 - See all books
0 - Exit
: """))

    # Add new book to the database
    if menu == 1:
        book_title = input("Enter the book's title: ")
        book_author = input("Enter the book's author: ")
        book_qty = int(input("Enter the quantity of the book with this title available: "))
        book_id = 1 + find_last_id()

        cursor.execute("""INSERT INTO bookstore(id, Title, Author, Qty)
                          VALUES(?, ?, ?, ?)""", (book_id, book_title, book_author, book_qty))
        db.commit()

        print("The new book has been successfully added to the shelf!")

    # Update book in the database
    elif menu == 2:
        book_id = input("Choose the book by entering its ID: ")

        update_choice = input("What do you want to update? (Title, Author, Quantity): ").upper()

        # Update the book's title
        if update_choice == "TITLE":
            book_title = input("Enter new book's title: ").capitalize()

            cursor.execute("""UPDATE bookstore SET Title = ? WHERE id = ?""", (book_title, book_id))
            print("Book's title updated!")

        # Update the book's author
        elif update_choice == "AUTHOR":
            book_author = input("Enter new book's author: ").capitalize()

            cursor.execute("""UPDATE bookstore SET Author = ? WHERE id = ?""", (book_author, book_id))
            print("Book's author updated!")

        # Update the quantity of the book available
        elif update_choice == "QUANTITY":
            book_qty = int(input("Enter new quantity: "))

            cursor.execute("""UPDATE bookstore SET Qty = ? WHERE id = ?""", (book_qty, book_id))
            print("Book's quantity updated!")

        else:
            print("Invalid input!")

    # Delete a book from the database
    elif menu == 3:
        book_id = input("Choose the book by entering its ID: ")

        cursor.execute("""DELETE FROM bookstore WHERE id = ?""", (book_id,))
        print(f"Book with ID{book_id} has been deleted!")

    # Choose a book from the database
    elif menu == 4:
        book_id = input("Choose the book by entering its ID: ")

        cursor.execute('''SELECT id, Title, Author, Qty FROM bookstore WHERE id = ?''', (book_id,))
        show_in_table()

    # Show all books in database
    elif menu == 5:
        # Show the bookshelf
        cursor.execute('''SELECT id, Title, Author, Qty FROM bookstore''')
        show_in_table()

    # Exit the program
    elif menu == 0:
        print("Goodbye!")
        exit()

    else:
        print("Invalid input! Try again.")
