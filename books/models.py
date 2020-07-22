from django.db import models

from authors.models import Author

#Relación uno a muchos con autores
#la consulta de la relacion será  -> model en minuscula_ set    ->   elizabeth.book_set.count()   , elizabeth.book_set.filter(title='it')  donde elizabeth es la autora del libro
#puedo poner en la clave foranea, despues del CASCADE. related_name='books' , entonces ya no tendré que usar book_set(Ahora la relación se llama books) sino que usamos elizabeth.books.count(). Pero para eso tengo que hacer la migración de vuelta.

class Book(models.Model):
    title = models.CharField(max_length=50)

    author = models.ForeignKey(Author,on_delete=models.CASCADE) #uno a muchos. Cuando un autor se elimine tambien lo haga la relación con los libros. Si se borra un autor se borrarán los libros de ese autor en la bd

    pages = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#La fundación - Yo Robot - La ultima pregunta, IT, El resplando, la torre oscura