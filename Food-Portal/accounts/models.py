from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Verificated_Code(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.IntegerField()
    
    def __str__(self):
        return self.email
	