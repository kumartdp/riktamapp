"""riktamapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views



urlpatterns = [
   

    path('',views.login1,name='home'),
    path('login1',views.login1,name='home'),
    path('login',views.login,name='home'),
   
    path('register',views.register,name="register"),

    
    
    path('image_upload/<str:session>',views.hotel_image_view, name = 'image_upload'), 
    path('success/<str:session>', views.success, name = 'success'), 
    path('home/<str:session>', views.home), 
    path('my/<str:session>',views.my), 
    path('success/image_upload/image_upload/success/<str:session>',views.hotel_image_view, name = 'image_upload'),
    path('delete/<int:id1>',views.delete),
    path('edit/<int:id1>/<str:session>',views.edit),
    path('upvote/<int:id1>/<str:session>',views.upvote),
    
    

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





