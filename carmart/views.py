from django.shortcuts import render,redirect
from car.models import CarModel
from car.models import BrandModel
def home(request,category_slug=None):
    cars=CarModel.objects.all()
    brands=BrandModel.objects.all()
    if category_slug is not None:
        brand=BrandModel.objects.get(slug=category_slug)
        cars=CarModel.objects.filter(brand_name=brand)
    return render(request,'home.html',{'cars':cars,'brands':brands})
