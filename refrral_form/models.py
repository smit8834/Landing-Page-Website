from django.db import models

class FORM(models.Model):
    name= models.CharField(max_length= 20)
   # DOB= models.DateField(null=True) 
    EMAIL= models.EmailField(null=True)
    COURSE=models.CharField(max_length= 30)
    #YEAR= models.IntegerField()
    CONTACT_NUM=models.IntegerField()
    #WHATSAPP=models.IntegerField()
    COLLEGE=models.CharField(max_length=200)
    ####RRED_BY=models.CharField(max_length=200,null=True,blank=True)

