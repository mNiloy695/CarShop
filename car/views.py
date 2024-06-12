from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import CarModel
from car.models import commnetsModel
from .models import Buy
from django.shortcuts import render,redirect
from car.forms import commentsForm
@login_required
def buy(request,id):
    car=CarModel.objects.get(pk=id)
    if car.quantity>0:
        car.quantity-=1
        car.save()
        Buy.objects.create(car=car,user=request.user)
        return redirect('home')
    else:
        return redirect('home')

def details(request,id):
    car=CarModel.objects.get(pk=id)
    comments=commnetsModel.objects.filter(car=car)
    if request.method =='POST':
        form=commentsForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.car=car
            comment.save()
            return redirect('details',id=id)
    else:
        form=commentsForm()
    return render(request,'details.html',{'car':car,'form':form,'comments':comments})






