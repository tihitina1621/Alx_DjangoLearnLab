to update the title of the book instance:

record = Book.objets.get(id=1)
record.title = "Nineteen Eighty-Four"
record.save()     #the title field is updates from 1984 to Nineteen Eighty-Four.