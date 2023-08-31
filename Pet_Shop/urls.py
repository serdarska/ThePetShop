from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Pets.views import *
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="index"),
                  path('login/', login, name="login"),
                  path('register/', register, name='register'),
                  path('item/add/toy/', addDogToy, name='addDogToy'),
                  path('item/add/food/', addDogFood, name='addDogFood'),
                  path('item/add/bed/', addDogBed, name='addDogBed'),
                  path('item/add/collar/', addDogCollar, name='addDogCollar'),
                  path('about/', aboutus, name="aboutus"),
                  path('contact/', contactus, name="contactus"),
                  path('dogBeds/', DogBeds, name="DogBeds"),
                  path('dogFoods/', DogFoods, name="DogFoods"),
                  path('dogToys/', DogToys, name="DogToys"),
                  path('dogCollars/', DogCollars, name="DogCollarAndLeash"),
                  path('catToys/', CatToys, name="CatToys"),
                  path('catFood/', CatFoods, name="CatFoods"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
