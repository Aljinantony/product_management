from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_code=models.CharField(max_length=50,unique=True)
    cateogery=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.PositiveBigIntegerField()
    def __str__(self):
        return self.product_name