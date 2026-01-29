from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Restaurant,Item
# Create your views here.
def index(request):
    return render(request, "index.html")

def open_sign_in(request):
    return render(request,'sign_in.html')

def open_sign_up(request):
    return render(request,'sign_up.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        
        # optional validation 
        # more robust application , you can 
        # the from data before saving it to database
        if User.objects.filter(email=email).exists():
            return HttpResponse("This is email is alraedy registered . please use a different email.")
        
        
    #  the database to the data 
        user = User(
        username=username,   # lowercase
        password=password,
        email=email,
        mobile=mobile,
        address=address
        )

    # to the data in the database 
        user.save()

        # after succesds fully sign up it will direct render to the sign in
        # not to print sign is sucess fully and set the path in the urls .py
        # return HttpResponse("Sign up successful and the data is saved")
        return render(request, 'sign_in.html')
    else:
        return HttpResponse("Invalid response")
    
    # request method should to the sign
def sign_in(request):
    # user ="ashwith"
    # pwd=123
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
    try: 
        User.objects.get(username=username, password=password)     
        if username=="admin":
            return render(request, 'admin.html')
        else:
            restaurantList=Restaurant.objects.all()
            return render(request, 'customer.html', {"restaurantList" : restaurantList  ,"username" : username})
    except User.DoesNotExist:
        return render(request, 'failed.html')
        

def open_add_restaurant(request):
    return render(request, 'add_restaurant.html')

# objects = the tool Django gives you to talk to the database

# .get(), .create(), .filter() = database operations 
# Restaurant.objects   means:

# “Give me access to the Restaurant table in the database.”
# 

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        # rating = request.POST.get('rating')
        rating = float(request.POST.get('rating'))

        try:
            Restaurant.objects.get(name = name)
            return HttpResponse("Duplicate restaurant!")
            
        except:
            Restaurant.objects.create(
                name = name,
                picture = picture,
                cuisine = cuisine,
                Rating = rating,
            )
        return HttpResponse("Successfully Added !")
        # return render(request, 'admin_home.html')
#  function should equal to the views path 
def open_show_restaurant(request):
    # to render the data in the show_restaurant in the data base 
    restaurantList=Restaurant.objects.all()
    return render(request, 'show_restaurant.html',{'restaurantList' :restaurantList})


def update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'update_restaurant.html', {'restaurant': restaurant})

def open_update_restaurant(request,restaurant_id):
    restaurant= Restaurant.objects.get(id=restaurant_id)
    return render(request, 'update_restaurant.html',{'restaurant' : restaurant})

# def open_update_restaurant(request,restaurant_id):
#     restaurant= Restaurant.objects.get(id=restaurant_id)
#     return render(request, 'update_restaurant.html',{'restaurant' : restaurant})

def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    itemList = restaurant.items.all()
    #itemList = Item.objects.all()
    return render(request, 'update_menu.html',{"itemList" : itemList, "restaurant" : restaurant})

def update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vegeterian = request.POST.get('vegeterian') == 'on'
        picture = request.POST.get('picture')
        
        try:
            Item.objects.get(name = name)
            return HttpResponse("Duplicate item!")
        except:
            Item.objects.create(
                restaurant = restaurant,
                name = name,
                description = description,
                price = price,
                vegeterian = vegeterian,
                picture = picture,
            )
    # return render(request, 'admin_home.html')
    return HttpResponse("added")
    