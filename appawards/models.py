from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField


# Create your models here.

class Profile(models.Model):

    bio = HTMLField()
    profile_pic = models.ImageField(upload_to = 'image/', blank=True, null=True)
    full_name = models.CharField(max_length=60)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    email=models.EmailField()
    phone_number = models.CharField(max_length =30,blank =True)
    # user_project=models.ForeignKey(Project, on_delete=models.CASCADE)
    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id=id).update(user_id = new_user)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user
