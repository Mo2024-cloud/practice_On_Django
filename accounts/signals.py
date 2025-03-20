from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a new User is saved, this function runs
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # Check if this is a new user
        Profile.objects.create(user=instance)  # Create a Profile for this user


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # Save the Profile whenever the User is updated


"""
    Django doesn’t automatically detect signals.py, so we need to connect it.

🔹  Open accounts/apps.py and modify the ready() method like this:
"""
