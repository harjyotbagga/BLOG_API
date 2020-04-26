from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        #FirstName, LastName, Username, Password, Email
    #Later add a profile pic section.

    def __str__(self):
        return self.user.username

    # User Model Fields
    #   -first_name
    #   -last_name
    #   -username
    #   -password
    #   -email
