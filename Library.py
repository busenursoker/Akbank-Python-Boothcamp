class Library:
    
    def __init__(self):
        self.file = "books.txt"

    def __del__(self): 
         self.file.close()
    
    def add_books(self):
        book_title = input("Enter the title of the book please :")
        book_author = input("Enter the author of the book please :")
        release_year = input("Enter the relese year of the book please :")
        num_pages = input("Enter the number of pages of the book please: ")
        book_genre = input("Enter the genre of the book please :")
        book_info = f"{book_title},{book_author},{book_genre},{release_year},{num_pages}\n"

        with open(self.file, "a") as f:
            f.write(book_info)
        print("Book added to your library.")    
    
    def list_books(self):
        try:
            with open(self.file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    book_info = line.strip().split(',')
                    print(f"Book: {book_info[0]}, Author: {book_info[1]}")
        except FileNotFoundError:
            print("No books found.")


    def remove_book(self):
        book_title = input("Enter the title of the book to remove: ")
        try:
            with open(self.file, "r") as f:
                lines = f.readlines()
            with open(self.file, "w") as f:
                for line in lines:
                    if book_title not in line:
                        f.write(line)
            print("Book removed from your library.")
        except FileNotFoundError:
            print("No book found.")

        
lib = Library()

while True:
    print("\n")
    print("\nWELCOME TO YOUR LIBRARY!")
    print("What would you like to do?\n")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit\n")
    
    choice = input("Enter your choice please: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


