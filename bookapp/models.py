from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    pages=models.IntegerField()



    def __str__(self):
        return self.book_name


#ORM queries
#from bookapp.models import Book

#book=Book(book_name="randamoozham",author="mtvasudevan",price=180,pages=200)
#book.save()
#book=Book.objects.get(id=1)
#print(book.book_name)
#print(book.price)
#for book in books:
#...     print(book.book_name)
#...     print(book.price)


