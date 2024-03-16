from django.db import models
from users.models import User,BaseModel
from django .core.validators import FileExtensionValidator
from users.models import User


# Create your models here.
class Category(BaseModel):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='kategoriya'
        verbose_name_plural='kategoriyalar'

class Product(BaseModel):
    name=models.CharField(max_length=255)
    # users=models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='products')
    price=models.IntegerField(default=0)
    categor=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='proucts')
    decription=models.TextField(default='',null=True,blank=True)
    image=models.ImageField(upload_to='products_image',null=True,blank=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='mahsulot'
        verbose_name_plural='mahsulotlar'

class  Order(models.Model):
    order_id=models.CharField(unique=True,max_length=50)
    order_date=models.DateField(auto_now_add=True)
    total_price=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantitiy=models.PositiveIntegerField()
    def __str__(self):
        return str(self.order.order_id)

    def __str__(self) :
        return f"{self.name} --Quantitiy {self.quantitiy}"
    
    @property
    def total_price(self):
        return self.price*self.quantitiy
 