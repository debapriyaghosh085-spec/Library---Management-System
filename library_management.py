library = []
issued_books = []

def add_book():
    title = input("Enter your title : ")
    author = input("Enter author name: ")
    book ={"title " : title , "author" : author}
    library.append(book)
    print("Book added successfully !\n")

def display_book() :
    if not library :
        print("No book available .\n")
        return
    print("\n--- All Books ---")
    for i, book in enumerate (library, 1):
        print(f"{i}. {book['title']} by {book['author']}\n")
    print()

def search_book():
    title = input("Enter book title to issue: ")
    found = False
    for book in library :
        if book ["title"].lower() == title.lower() :
            print(f"Book Found : {book['title']} by {book['author']}\n")
            found = True
            break
    if not found :
        print("Book not found.\n")

def issue_book():
    title = input("Enter book title to issue: ")
    for book in library :
        if book ["title"].lower() == title.lower() :
            issued_books.remove(book)
            library.append(book)
            print("Book issued successfully! \n")
            return
    print("This book was not available. \n")

def return_book():
    title = input("Enter book title to return: ")
    for book in library :
        if book ["title"].lower() == title.lower() :
            issued_books.remove(book)
            library.append(book)
            print("Book returned successfully! \n")
            return
    print("This book was not issued . \n")




while True :
    print("==== Library Menu ===")
    print("1. Add Book")
    print("2. Display Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1" :
        add_book()
    elif choice == "2" :
        display_book()
    elif choice == "3" :
        search_book()
    elif choice== "4" :
        issue_book()
    elif choice == "5" :
        return_book ()
    elif choice == "6" :
        print("Exiting program...")
        break
    else:
        print("Invalid choice . Try again . \n")
    

