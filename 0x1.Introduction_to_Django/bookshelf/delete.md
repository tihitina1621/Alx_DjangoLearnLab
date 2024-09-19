to delete the instance we created

records = Book.objects.get(id=1)
records.delete()     #the instance we created ha been deleted