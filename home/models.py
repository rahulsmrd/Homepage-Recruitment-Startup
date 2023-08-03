from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User as mainUser

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
    
class profile(models.Model):
    user=models.OneToOneField(mainUser,related_name="profile", on_delete=models.CASCADE)
    recruiter=models.BooleanField(default=False)
    finder=models.BooleanField(default=False)

    def recruited(self):
        if self.recruiter:
            return True
        return False
    
    def __str__(self) -> str:
        return self.user.username
    
class posts(models.Model):
    name=models.CharField(max_length=200)
    post_designation=models.CharField(max_length=300)
    experience=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.post_designation