from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import DogBed, DogFood, DogCollar, DogToy, CatFood, CatToy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import DogFoodForm, DogToyForm, DogBedForm, DogCollarForm, CatToyForm, CatFoodForm



# Create your views here.
def index(request):
    queryset = DogCollar.objects.all()
    context = {"collars": queryset}
    return render(request, "index.html", context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return redirect('index')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid login credentials.'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def addDogFood(request):
    if request.method == 'POST':
        form = DogFoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DogFoods')  # Redirect to the cart or any other appropriate URL
    else:
        form = DogFoodForm()
    return render(request, 'addDogFood.html', {'form': form})

def addDogToy(request):
    if request.method == 'POST':
        form = DogToyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DogToys')  # Redirect to the cart or any other appropriate URL
    else:
        form = DogToyForm()
    return render(request, 'addDogToy.html', {'form': form})

def addDogBed(request):
    if request.method == 'POST':
        form = DogBedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DogBeds')  # Redirect to the cart or any other appropriate URL
    else:
        form = DogBedForm()
    return render(request, 'addDogBed.html', {'form': form})

def addDogCollar(request):
    if request.method == 'POST':
        form = DogCollarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DogCollarAndLeash')  # Redirect to the cart or any other appropriate URL
    else:
        form = DogCollarForm()
    return render(request, 'addDogCollar.html', {'form': form})

def aboutus(request):
    return render(request, "aboutus.html")


def contactus(request):
    return render(request, "contactus.html")


def DogBeds(request):
    queryset = DogBed.objects.all()
    context = {"beds": queryset}
    return render(request, "DogBeds.html", context=context)


def DogFoods(request):
    queryset = DogFood.objects.all()
    context = {"foods": queryset}
    return render(request, "DogFood.html", context=context)


def DogCollars(request):
    queryset = DogCollar.objects.all()
    context = {"collars": queryset}
    return render(request, "DogCollarAndLeash.html", context=context)


def DogToys(request):
    queryset = DogToy.objects.all()
    context = {"toys": queryset}
    return render(request, "DogToys.html", context=context)


def CatToys(request):
    queryset = CatToy.objects.all()
    context = {"toys": queryset}
    return render(request, "CatToys.html", context=context)


def CatFoods(request):
    queryset = CatFood.objects.all()
    context = {"foods": queryset}
    return render(request, "CatFood.html", context=context)
