from django.contrib import admin
from .models import products
# Register your models here.

admin.site.register(products)

# make migrations
# migrate --database=products_db
# python manage.py migrate --run-syncdb (imp) 