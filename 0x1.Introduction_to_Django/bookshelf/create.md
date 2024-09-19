To creat a Book indtance:

python manage.py shell                  #access the django shell command
from bookshelf.models import Book       #my Book model has been imported
new_record = Book(title = "1984", author = "George Orwell", publication_year = 1949)   
new_record.save()                       #new Book instances is created and saved