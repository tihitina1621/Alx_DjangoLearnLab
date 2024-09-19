from relationship_app.models import Book, Author

all_book = Book.objects.all()
print(all_book)

author = Author.objects.filter(name="James")
book_author = Book.objects.filter(authors = author)