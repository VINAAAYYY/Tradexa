from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateField()
    updated_at = models.DateField(blank=True)
    def __str__(self):
        return self.name