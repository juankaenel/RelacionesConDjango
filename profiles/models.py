#Django
from django.db import models
#Local
from authors.models import Author

#Relacion uno a uno con author

class Profile(models.Model):
    alias = models.CharField(max_length=50)
    author = models.OneToOneField(Author,on_delete=models.CASCADE, related_name='profile_author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alias