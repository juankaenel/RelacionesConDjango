#Django
from django.db import models

#Local
from books.models import Book
from authors.models import Author

#Relación muchos a muchos con libros

class Gender(models.Model):
    name = models.CharField(max_length=50)
    #el atributo va en plural pq son muchos libros
    books = models.ManyToManyField(Book) #esta es una forma. esta forma ya me crea la tabla de la relacion con los atributos book_id y gender_id automaticamente como claves foraneas

    #esta es la otra forma de una relacion muchos a muchos pero con autores
    authors = models.ManyToManyField(Author, through='AuthorGender')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#acá creo la tabla de la relacion con los autores
class AuthorGender(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE) #gender_id
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #author_id
    quantity = models.IntegerField(default=1) #este atributo me indica la cantidad q hay en la relacion

#la segunda forma se usa cuando queremos tener atributos extras en la tabla, como por ejemplo quantity, caso que no se puede hacer con la primer forma pq ya crea la tabla automaticamente