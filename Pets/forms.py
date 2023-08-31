from django import forms
from .models import *


class DogFoodForm(forms.ModelForm):
    class Meta:
        model = DogFood
        fields = ['title', 'description', 'image',  'price']


class DogToyForm(forms.ModelForm):
    class Meta:
        model = DogToy
        fields = ['title', 'description', 'image',  'price']

class DogCollarForm(forms.ModelForm):
    class Meta:
        model = DogCollar
        fields = ['title', 'description', 'image',  'price']

class DogBedForm(forms.ModelForm):
    class Meta:
        model = DogBed
        fields = ['title', 'description', 'image',  'price']

class CatToyForm(forms.ModelForm):
    class Meta:
        model = CatToy
        fields = ['title', 'description', 'image',  'price']

class CatFoodForm(forms.ModelForm):
    class Meta:
        model = CatFood
        fields = ['title', 'description', 'image',  'price']