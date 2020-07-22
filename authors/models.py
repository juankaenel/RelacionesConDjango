from django.db import models

#Relación uno a muchos con libros
# Author.objects.filter(book__title='it')   -> dame el autor de ese libre
# Author.objects.filter(book__title__startwith='it') #el modelo libro tiene el atributo title y que empieza con it
class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

