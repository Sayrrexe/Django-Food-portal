from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_subscribers = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author_user}'


class Recept(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    ccal = models.IntegerField(default=0)
    post_rating = models.SmallIntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dis_like(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.text[0:50] + '...'

    def __str__(self):
        return f"{self.title} by {self.author.author_user.username}"

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Comment(models.Model):
    commentRecept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dis_like(self):
        self.rating -= 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    Author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )