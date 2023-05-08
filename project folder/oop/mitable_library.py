class Library:
    '''represent library'''
    def __init__(self, books = []):
        """int library items"""
        #self.books = [] 
        self.books = books

    def add_books(self, book):
        '''add book'''
        self.books.append(book)


london = Library(['War and Peace'])

london.add_books("Clear code")
london.add_books("Python")

print(london.books)

new_york = Library()
new_york.add_books("java 8")

print(new_york.books)
print(london.books)