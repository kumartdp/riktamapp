from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import GetImage 
import mysql.connector
# Create your views here.



def login(request):
    
    username=request.POST['username']
    password=request.POST['password']
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="internet"
            )

    mycursor = mydb.cursor()
    mycursor.execute("select * from register")
    rows=mycursor.fetchall()
    flag=0
    k=0
    for r in rows:
        if(username==r[1] and password==r[4]):
            flag=1
            k=r[1]
            break
    if(flag==1):
        return redirect('success',session=k)
def home(request,session):
    l=session
    return redirect('success',session=l)


        
    



def login1(request):
    return render(request,'login.html')
def register1(request):
    return render(request,'register.html')
    
def register(request):
    
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    cpassword=request.POST['confirm_password']
    location=request.POST['location']
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="internet"
            )

    mycursor = mydb.cursor()
    sql = "INSERT INTO register (fname,lname,email,password,location) VALUES (%s, %s,%s,%s,%s)"
    val = (fname,lname,email,password,location)
    mycursor.execute(sql, val)
    return redirect('login1')
def hotel(request): 
    return render(request,'login.html')
def my(request,session):
    allimages = Hotel.objects.filter(username=session)
    l1=[]
    l1.append(session)
    return render(request, 'showmy.html',{'images' : allimages},{'session':l1})



def hotel_image_view(request,session): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success/session') 
    else: 
        form = HotelForm() 
    l2=[]
    l2.append(session)
    return render(request, 'addissue.html', {'form' : form},{'sesssion':l2}) 
  
  
def success(request,session): 
    allimages = Hotel.objects.all()
    l1=[]
    l1.append(session)
    return render(request, 'show.html',{'images' : allimages},{'session':l1})
    