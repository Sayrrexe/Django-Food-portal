from django.contrib import admin
from .models import Recept, Author, Subscription


admin.site.register(Author)
admin.site.register(Recept)
admin.site.register(Subscription)