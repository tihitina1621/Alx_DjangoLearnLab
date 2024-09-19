from relationship_app.models import Book, Author, Library, Librarian


neew = Librarian.objects.get(library="name")

author_name = 'James'
author = Author.objects.get(name=author_name)
all = Book.objects.filter(author=author)

library_name = 'new'
library = Library.objects.get(name=library_name) 
all_book = library.books.all()
print(all_book)