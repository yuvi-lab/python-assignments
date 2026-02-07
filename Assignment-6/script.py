class Library:
    def __init__(self, book_name, author):
        # Instance variables
        self.book_name = book_name
        self.author = author
        self.is_available = True  # Book is available by default

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f'"{self.book_name}" has been successfully checked out.')
        else:
            print(f'Sorry, "{self.book_name}" is currently not available.')

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f'"{self.book_name}" has been successfully returned.')
        else:
            print(f'"{self.book_name}" was not checked out.')

    def display_status(self):
        status = "Available" if self.is_available else "Checked Out"
        print(f'Book: {self.book_name}')
        print(f'Author: {self.author}')
        print(f'Status: {status}')
        print("-" * 40)



# Creating book objects
book1 = Library("The Alchemist", "Paulo Coelho")
book2 = Library("1984", "George Orwell")

# Display initial status
print("\nInitial Book Status:")
book1.display_status()
book2.display_status()

# Checkout a book
print("\nChecking out Book 1:")
book1.check_out()

# Try checking out the same book again
book1.check_out()

# Return the book
print("\nReturning Book 1:")
book1.return_book()

# Display final status
print("\nFinal Book Status:")
book1.display_status()
book2.display_status()


