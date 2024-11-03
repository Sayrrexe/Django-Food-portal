from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author

@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(author_user=instance)
