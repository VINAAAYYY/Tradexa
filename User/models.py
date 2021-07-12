from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.AutoField
    username = models.CharField('username', max_length=50)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name',max_length=50, blank=True)
    email = models.EmailField('example@website.com')
    password = models.CharField(max_length = 300)
    

    def __str__(self):
        return self.username

class post(models.Model):
    user = models.ForeignKey(user, default=1, on_delete=models.PROTECT, blank=True)
    texts = models.CharField('Enter text', max_length=3000, default="")
    created_at = models.DateField('created at')
    updated_at = models.DateField('updated at')

