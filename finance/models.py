from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Account(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    remain = models.DecimalField(max_digits=12, decimal_places=0,default=0)
    
    
class Transaction(models.Model):
    
    class TransactionType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"
    
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=0,validators=[MinValueValidator(1)])
    date = models.DateField()
    type = models.CharField(
           max_length=7,
           choices=TransactionType.choices)
    category = models.ForeignKey(Category,on_delete= models.SET_NULL,null=True,blank=True,)
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,blank=True,)