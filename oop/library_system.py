class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.name}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author, file_size)
        
    def __str__(self):
        return f"{self.title} by {self.name}, File Size: {self.file_size}"
        
    #def __init__(self, file_size):
        #self.file_size = file_size
        
class PrintBook(Book):
    def __init__(self, title, author, page_count, books):
        super().__init__(title, author, page_count, books)
        
    def __str__(self):
        return f"{self.title} by {self.name}, File Size: {self.file_size}"
        
class Library:
    def __init__(self, books):
        self.books = books
        
    def add_book(self, book):
        self.books = []

        if self.book == Book():
            self.books.append(book)
            
        elif self.book == EBook():
            self.books.append(book)
            
        elif self.book == PrintBook():
            self.books.append(book)
            
    def list_books(self, books):
        self.books = books
        if self.books == Book():
            print(f"{self.title} by {self.name}")
            
        elif self.books == EBook():
            print(f"{self.title} by {self.name}, File Size: {self.file_size}")
            
        elif self.books == PrintBook():
            print(f"{self.title} by {self.name}, Page Count: {self.page_count}")
        
        
    
    
        