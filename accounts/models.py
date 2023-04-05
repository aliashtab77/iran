from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class ProfileModel(models.Model):
    class Meta:
        verbose_name_plural = "کاربران"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    phone = PhoneNumberField(region='IR', verbose_name="تلفن همراه")
    # rule = models.BooleanField(default=False)
    # man = 1
    # woman = 2
    # status_choices = ((man, "مرد"), (woman, 'زن'))
    # gender = models.IntegerField(choices=status_choices, default=1)
    avatar = models.ImageField(upload_to="profiles", null=True)
    def __str__(self):
        return self.user.username




