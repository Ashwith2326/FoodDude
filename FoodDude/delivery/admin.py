from django.contrib import admin
from .models import User
from .models import Restaurant
from .models import Item  


# Register your models here.
admin.site.register(User)

# database table
admin.site.register(Restaurant)

# if it is name is item the django will crash
admin.site.register(Item)