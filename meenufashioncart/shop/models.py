from django.db import models

# Create your models here.

class Product(models.Model):
    Product_ID = models.AutoField
    Product_Name = models.CharField(max_length=50)
    Product_Description = models.CharField(max_length=300)
    Category = models.CharField(max_length=50)
    Sub_Category = models.CharField(max_length=50)
    Publish_Date = models.DateField()
    Image = models.ImageField(upload_to='static/shop/images')


    def __str__(self):
        return self.Product_Name    

