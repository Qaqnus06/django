from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.core.validators import FileExtensionValidator


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


CUSTOMER,EMPLOYEE,ADMIN=('customer','employee','admin')


class User(AbstractUser):
    USER_ROLE=(
        (CUSTOMER,CUSTOMER),
        (EMPLOYEE,EMPLOYEE),
        (ADMIN,ADMIN)
    )


    phone_number=models.CharField(max_length=255,unique=True,null=True, blank=True)
    bio=models.CharField(max_length=255,null=True, blank=True)
    user_role=models.CharField(max_length=25,choices= USER_ROLE, default=CUSTOMER)
    email=models.EmailField(max_length=255,unique=True,null=True, blank=True)
    photo=models.ImageField( upload_to='users_image/',null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jepg'])])


    def __str__(self):
        return self.username

