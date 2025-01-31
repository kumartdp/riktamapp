from django.db import models 
class Hotel(models.Model): 
    username=models.CharField(max_length=50)

    location = models.CharField(max_length=50) 
    imgurl=models.CharField(max_length=50)



    hotel_Main_Img = models.ImageField(upload_to='images/',default="")
    count=models.IntegerField(default=0)
    
    status = models.CharField(max_length=50,default="open") 
    issuetitle=models.CharField(max_length=50)
    


class GetImage(models.Model):   
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media")
    class Meta:
        db_table="riktamapp_getimage"
