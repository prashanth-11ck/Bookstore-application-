class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        book = {"title": title, "author": author, "price": price}
        self.books.append(book)
        print(f'Book "{title}" added successfully!')

    def view_books(self):
        if not self.books:
            print("No books available in the store.")
        else:
            print("\nList of books:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
        if results:
            print("\nSearch results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, Price: {book['price']}")
        else:
            print("No books found matching your search.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f'Book "{title}" removed successfully.')
                return
        print(f'Book "{title}" not found in the store.')

def main():
    store = Bookstore()

    while True:
        print("\n=== Book Store Menu ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = input("Enter book price: ")
            store.add_book(title, author, price)
        elif choice == "2":
            store.view_books()
        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            store.search_book(keyword)
        elif choice == "4":
            title = input("Enter the title of the book to remove: ")
            store.remove_book(title)
        elif choice == "5":
            print("Exiting the book store app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
