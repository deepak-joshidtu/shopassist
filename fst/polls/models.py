from django.db import models

from djangotoolbox.fields import ListField
class infiitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      amzlink=models.TextField()
      list_url=models.TextField()
      amzimg=models.TextField()
      price=models.CharField(max_length=50)
      brand=models.CharField(max_length=50)
      features=models.TextField()
      title=models.CharField(max_length=50)
      allkeyw=models.TextField()
      osource=models.CharField(max_length=50)
      catval=models.IntegerField(default=0)
      scatval=models.CharField(max_length=150)
      pdgrp=models.IntegerField(default=0)
      spid=models.CharField(max_length=50)
      created = models.DateTimeField(null=True,blank=True)
      cprice=models.CharField(max_length=50)
      def searchin(self,t):
          lst=[]
          a=infiitems.objects.filter(allkeyw__icontains=t).all()
          if a:
              return "true"
          return "false"

class ptmitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      amzlink=models.TextField()
      cprice=models.CharField(max_length=50)
      amzimg=models.TextField()
      price=models.IntegerField()
      brand=models.CharField(max_length=50)
      title=models.CharField(max_length=250)
      allkeyw=models.TextField()
      osource=models.CharField(max_length=50)
      catval=models.IntegerField(default=0)
      scatval=models.CharField(max_length=150)
      pdgrp=models.IntegerField(default=0)
      spid=models.CharField(max_length=50)
      created = models.DateTimeField(null=True,blank=True)
      def searchin(self,t):
          a=ptmitems.objects.filter(allkeyw__icontains=t).all()
          if a:
              return "true"
          return "false"

class snapitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      amzlink=models.TextField()
      amzimg=models.TextField()
      price=models.CharField(max_length=50)
      list_url=models.TextField()
      allkeyw=models.TextField()
      cprice=models.CharField(max_length=50)
      osource=models.CharField(max_length=50)
      catval=models.IntegerField(default=0)
      pdgrp=models.IntegerField(default=0)
      spid=models.CharField(max_length=50)
      created = models.DateTimeField(null=True,blank=True)
      def searchin(self,t):
          a=snaptems.objects.filter(allkeyw__icontains=t).all()
          if a:
              return "true"
          return "false"

class colorcounts(models.Model):
      colorcategory=models.CharField(max_length=200)
      colorcount=models.IntegerField(default=0)
class brandcounts(models.Model):
      brandcategory=models.CharField(max_length=200)
      brandcount=models.IntegerField(default=0)

class flipitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      amzlink=models.TextField()
      amzimg=models.TextField()
      price=models.IntegerField()
      brand=models.CharField(max_length=50)
      color=models.CharField(max_length=50)
      cprice=models.CharField(max_length=50)
      features=models.TextField()
      title=models.CharField(max_length=50)
      colorv=models.CharField(max_length=50)
      sizev=models.CharField(max_length=50)
      productid=models.CharField(max_length=50)
      blk=models.IntegerField()
      spid=models.CharField(max_length=50)
      osource=models.CharField(max_length=50)
      scatval=models.CharField(max_length=150)
      catval1=models.IntegerField(default=0)
      catval=models.IntegerField(default=0)
      pdgrp=models.IntegerField(default=0)
      created = models.DateTimeField(null=True,blank=True)

class metaitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      amzimg=models.TextField()
      brand=models.CharField(max_length=50)
      color=models.CharField(max_length=50)
      blk=models.IntegerField()
      colorvar=models.CharField(max_length=50)
      sizevar=models.CharField(max_length=50)
      pdgrp=models.IntegerField(default=0)
      grpprnt=models.IntegerField(default=1)
      catval=models.IntegerField(default=0)
      dispscore=models.IntegerField(default=0)
class blogs(models.Model):
      btitle= models.CharField(max_length=300)
      bcategory= models.CharField(max_length=100)
      btext=models.TextField()
      bcreatedby=models.CharField(max_length=300)
      btime=models.DateTimeField(null=True,blank=True)


class amznitems(models.Model):
      brandcategory= models.CharField(max_length=200)
      created = models.DateTimeField(null=True,blank=True)
      ahash= models.CharField(max_length=200)
      phash= models.CharField(max_length=200)
      dhash= models.CharField(max_length=200)
      imgtype=models.TextField()
      amzlink=models.TextField()
      itemlink1=models.TextField()
      itemlink2=models.TextField()
      itemlink3=models.TextField()
      itemlink4=models.TextField()
      amzimg=models.TextField()
      amzimg0=models.TextField()
      amzimg1=models.TextField()
      amzimg2=models.TextField()
      amzimg3=models.TextField()
      amzimg4=models.TextField()
      amzimg5=models.TextField()
      price=models.IntegerField()
      brand=models.CharField(max_length=50)
      color=models.CharField(max_length=50)
      binding=models.CharField(max_length=50)
      department=models.CharField(max_length=50)
      features=models.TextField()
      keywords=models.TextField()
      feakey=models.TextField()
      productgroup=models.CharField(max_length=50)
      size=models.CharField(max_length=50)
      title=models.CharField(max_length=50)
      height=models.IntegerField()
      width=models.IntegerField()
      length=models.IntegerField()
      weight=models.IntegerField()
      offerprice=models.IntegerField()
      blk=models.IntegerField()
      colorvar=models.CharField(max_length=50)
      sizevar=models.CharField(max_length=50)
      spid=models.CharField(max_length=50)
      sim0=models.CharField(max_length=50)
      sim1=models.CharField(max_length=50)
      sim2=models.CharField(max_length=50)
      sim3=models.CharField(max_length=50)
      sim4=models.CharField(max_length=50)
      asin=models.CharField(max_length=50)
      salesrank=models.IntegerField()
      osource=models.CharField(max_length=50)
      cprice=models.CharField(max_length=50)
      pdgrp=models.IntegerField(default=0)
      grpprnt=models.IntegerField(default=1)
      scatval=models.CharField(max_length=150)
      catval=models.IntegerField(default=0)
      dispscore=models.IntegerField(default=0)

class amznitems1(models.Model):
      brandcategory= models.CharField(max_length=200)
      created = models.DateTimeField(null=True,blank=True)
      amzlink=models.TextField()
      itemlink1=models.TextField()
      itemlink2=models.TextField()
      itemlink3=models.TextField()
      itemlink4=models.TextField()
      amzimg=models.TextField()
      amzimg0=models.TextField()
      amzimg1=models.TextField()
      amzimg2=models.TextField()
      amzimg3=models.TextField()
      amzimg4=models.TextField()
      amzimg5=models.TextField()
      price=models.IntegerField()
      brand=models.CharField(max_length=50)
      color=models.CharField(max_length=50)
      binding=models.CharField(max_length=50)
      department=models.CharField(max_length=50)
      features=models.TextField()
      keywords=models.TextField()
      feakey=models.TextField()
      productgroup=models.CharField(max_length=50)
      size=models.CharField(max_length=50)
      title=models.CharField(max_length=50)
      height=models.IntegerField()
      width=models.IntegerField()
      length=models.IntegerField()
      weight=models.IntegerField()
      offerprice=models.IntegerField()
      blk=models.IntegerField()
      colorvar=models.CharField(max_length=50)
      sizevar=models.CharField(max_length=50)
      spid=models.CharField(max_length=50)
      sim0=models.CharField(max_length=50)
      sim1=models.CharField(max_length=50)
      sim2=models.CharField(max_length=50)
      sim3=models.CharField(max_length=50)
      sim4=models.CharField(max_length=50)
      asin=models.CharField(max_length=50)
      salesrank=models.IntegerField()
      osource=models.CharField(max_length=50)
      cprice=models.CharField(max_length=50)
      pdgrp=models.IntegerField(default=0)
      grpprnt=models.IntegerField(default=1)
      catval=models.IntegerField(default=0)
      dispscore=models.IntegerField(default=0)

class amzntables(models.Model):
    bagt=models.CharField(max_length=50)
    amzimg=models.TextField()
    brand=models.CharField(max_length=50)
    pid=models.CharField(max_length=50)
    brandcount=models.IntegerField(default=0)
    tablename=models.CharField(max_length=50)
    sbcat1=models.IntegerField(default=0)
    sbcat2=models.IntegerField(default=0)

class amzntables1(models.Model):
    bagt=models.CharField(max_length=50)
    tablename=models.CharField(max_length=50)
    sbcat1=models.IntegerField(default=0)
    sbcat2=models.IntegerField(default=0)

class Post2(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = ListField()
    comments = ListField()

class myCollection(models.Model):
      Name=models.CharField(max_length=200)
      age=models.IntegerField()
      rolNo=models.IntegerField()

class myCollection2(models.Model):
      name=models.CharField(max_length=200)
      age=models.IntegerField()
      rollNo=models.IntegerField()

class myCollection3(models.Model):
      name=models.CharField(max_length=200)
      age=models.IntegerField()
      rollNo=models.IntegerField()
      class Meta:
        db_table = 'myCollection'





class Post5(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = ListField()
    comments = ListField()
# Create your models here
# Create your models here.
