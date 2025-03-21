from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
