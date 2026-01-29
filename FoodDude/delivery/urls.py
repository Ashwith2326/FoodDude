from django.contrib import admin
from django.urls import path
from . import views
# from django.urls import include


urlpatterns = [
    path('',views.index),
    path('open_sign_in/',views.open_sign_in, name='open_sign_in'),
    path('open_sign_up/',views.open_sign_up, name='open_sign_up'),
    path('sign_up/', views.sign_up , name="sign_up" ),
    #  after setting the path next def the sign in page in the views.py
    path('sign_in/', views.sign_in , name="sign_in" ),
    
    
    # below url is not the html page is the just url   to open the open_add_restaurant 
    # open open_add_restaurant href to the admin to add new restaurant
    
    path('open_add_restaurant/', views.open_add_restaurant, name='open_add_restaurant'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('open_show_restaurant/', views.open_show_restaurant, name='open_show_restaurant'),
    path('open_update_menu/<int:restaurant_id>', views.open_update_menu, name='open_update_menu'), 
    path('update_menu/<int:restaurant_id>', views.update_menu, name='update_menu'),
    
]