from django.db import models
import uuid, datetime
from shop.models import Praduct


PAYMANT_CHOICS=(
        ('CASH,','CASH'), 
        ('CARD','CARD'),
)

class Costomer(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Shopcard(models.Model):
    PAYMANT_CHOICS=(
            ('CASH,','CASH'), 
            ('CARD','CARD'),
    )
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())
    praduct = models.ManyToManyField(Praduct,related_name='Praduct', blank=True)
    owner = models.ForeignKey(Costomer, related_name="Costomer", on_delete=models.CASCADE)
    paymant = models.CharField(max_length=10, choices=PAYMANT_CHOICS, default="CARD")

    def __str__(self) -> str:
        return self.owner.name
    
    def get_total_price(self):
        productt :Praduct
        a = 0
        for productt in self.praduct.all():
            a += productt.price
        return a





