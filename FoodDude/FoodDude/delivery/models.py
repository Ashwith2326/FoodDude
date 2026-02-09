# what are the modele we are created the can be register in the admin.py 
# the models are created for the table to store the render page the data 
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=15 , default="")
    address = models.TextField()


    def __str__(self):
        return self.username

# after creating  the Restaurant register the model in the admin.py
class Restaurant(models.Model):
    name=models.CharField(max_length=50)
    picture=models.URLField( max_length=500, default='https://b.zmtcdn.com/data/pictures/2/20565372/bccf6cabc04a24fa6c4ccfbb56ac6a99_featured_v2.jpg')
    cuisine=models.CharField(max_length=200)
    Rating =models.FloatField()
    
    def __str__(self):
        return self.name
    
# to update the menu in the list
# function should start with capital letter 
class Item(models.Model):
    # below line the SQL line in the dataase
    # and the below frame the relation b/w the restaurant and the item table in the SQL ot database table
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = "items")
    name= models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length = 400, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')

    def __str__(self):
        return self.name