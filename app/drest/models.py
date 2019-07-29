from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Lno(models.Model):
    lno = models.CharField(max_length=8, unique=True, verbose_name="lottery")
    cname = models.CharField(max_length=100)
    reseller = models.ForeignKey('auth.User', related_name='reseller', on_delete=models.CASCADE, )
    contact = models.CharField(max_length=200, )
    address = models.CharField(max_length=200, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.lno

    class Meta:
        ordering = ('created_at',)



