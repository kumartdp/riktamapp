from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import GetImage 
import mysql.connector
# Create your views here.


dup=''
def login(request):
    
    username=request.POST['username']
    password=request.POST['password']
    t=request.GET["type"]
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
        if(username==r[0] and password==r[3]):
            flag=1
            k=r[0]
            break
    if(flag==1):
        

        dup=k
        return redirect('/success'+'/'+k)
        

        
    else:

        return HttpResponse("invalid")
    else:
        if(t=="admin"):

            if(username=="admin" and password=="123"):
                return redirect('/successadmin')
            else:
                return HttpResponse("invalid")
        return HttpResponse("invalid")

def home(request,session):
    l=session
    return redirect('success',session=l)
def successadmin(request):
    allimages = Hotel.objects.filter(status="open")
    return render(request, 'adminshow.html',context={'images':allimages})




        
    



def login1(request):
    return render(request,'login.html')
    
def register(request):
    if request.method == "POST":
    

    
        fname=request.POST['f']
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
        print(fname,lname,email)
        sql = "INSERT INTO register (fname,lname,email,password,location) VALUES (%s, %s,%s,%s,%s)"
        val = (fname,lname,email,password,location)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

    
        return render(request,'login.html')
    else:
        return render(request,'register.html')
def hotel(request): 
    return render(request,'login.html')
def my(request,session):
    allimages = Hotel.objects.filter(username=session)
    l1=[]
    l1.append(session)
    return render(request, 'showmy.html',context={'images' : allimages,'session':l1})
def delete(request,id1):

    instance = Hotel.objects.get(id=id1)
    instance.delete()
    allimages = Hotel.objects.all()
    l1=[]
    l1.append(dup)
    
    return render(request, 'show.html',context={'images':allimages,'session':l1})
def edit(request,id1,session):

    instance = Hotel.objects.get(id=id1)
    instance.delete()
    

    
    return redirect('/image_upload'+'/'+session)
def upvote(request,id1,session):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="internet"
            )

    mycursor = mydb.cursor()
    mycursor.execute("select * from upvotes")
    rows=mycursor.fetchall()
    flag=1
    for r in rows:
        if(r[0]==id1 and r[1]==session):
            sql2="delete from upvotes where id=%s and username=%s"
            val2=(id1,session)
            mycursor.execute(sql2, val2)
            mydb.commit()



            flag=0
            break
    if(flag):
        sql="update riktamapp_hotel set count=count+%s where id=%s"
        val=(1,id1)
        mycursor.execute(sql, val)
        mydb.commit()

        sql1 = "INSERT INTO upvotes (id,username) VALUES (%s, %s)"
        val1 = (id1,session)
        mycursor.execute(sql1, val1)

        mydb.commit()
        mydb.close()
    else:
        sql="update  riktamapp_hotel set count=count-%s where id=%s"
        val=(1,id1)
        mycursor.execute(sql, val)
        
        mydb.commit()
        mydb.close()
    allimages = Hotel.objects.all()
    l1=[]
    l1.append(session)
    
    return render(request, 'show.html',context={'images':allimages,'session':l1})
def comment(request,id1,session):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="internet"
            )

    mycursor = mydb.cursor()
    
    sql = "select username,comment from comments "
    
    mycursor.execute(sql)
    row=mycursor.fetchall()
    r=[]
    for i in row:
        if(i[0]==id1):
            r.append(i)
    
    l1=[]
    l1.append(session)
    l2=[]
    l2.append(id1)
    return render(request,'comments.html',context={'data':r,'session':l1,'uid':l2})
def comment1(request,id1,session):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="internet"
            )

    mycursor = mydb.cursor()
    c=email=request.POST['com']
    
    sql = "insert  into comments (id,username,comment) values(%s,%s,%s)"
    val = (id1,session,c)
    mydb.commit()
    mydb.close()
    l1=[]
    l1.append(session)
    allimages = Hotel.objects.all()
    
    
    
    return render(request, 'show.html',context={'images':allimages,'session':l1})




    


        




    



def hotel_image_view(request,session): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            p=session
            return redirect('/success'+'/'+p) 
    else: 
        form = HotelForm() 
    l2=[]
    l2.append(session)
    
    return render(request, 'addissue.html',context={'form' : form,'session':l2}) 
  
  
def success(request,session): 
    allimages = Hotel.objects.all()
    l1=[]
    l1.append(session)
    
    return render(request, 'show.html',context={'images':allimages,'session':l1})
    