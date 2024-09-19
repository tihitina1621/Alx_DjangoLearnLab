from relationship_app.models import Book, Author, Library

all_book = Book.objects.all()
print(all_book)

author = Author.objects.filter(name="James")
book_author = Book.objects.filter(authors = author)

library = Library.objects.get(name='library_name') 
all_book = Book.objects.all(name = library)
print(all_book)