from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # on_delete -> In Django, when you create a ForeignKey relationship (e.g., linking the Profile model to Django’s built-in User model), you must specify what should happen when the referenced object (User) is deleted.
    # on_delete=models.CASCADE → If a user is deleted, their profile is also deleted automatically.
    """
    These options control whether a field can be left empty.

    blank=True → Allows the field to be empty in forms (not required in forms).
    null=True → Allows the field to be empty in the database (stores NULL instead of an empty string).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @staticmethod
    def get_or_create_profile(user):
        profile, created = Profile.objects.get_or_create(user=user)
        return profile
        """
        The get_or_create() method is a shortcut that retrieves an object if it exists or creates it if it doesn't.
        It returns a tuple (object, created), where created is a boolean indicating whether the object was created or retrieved.
        """
