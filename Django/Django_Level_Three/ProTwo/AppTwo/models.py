from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    emailid = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return str(self.emailid)
    



