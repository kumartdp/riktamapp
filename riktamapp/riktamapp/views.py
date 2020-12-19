from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import GetImage 
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'addissue.html', {'form' : form}) 
  
  
def success(request): 
    allimages = Hotel.objects.all()  
    return render(request, 'show.html',{'images' : allimages})
    