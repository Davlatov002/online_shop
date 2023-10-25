from django.db import models
import uuid, datetime

# Create your models here.
class Category(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self) -> str:
        return self.name

class Praduct(models.Model):
    id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='no-image.png')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    price = models.IntegerField(null=True, blank=True)
    start_data = models.DateField(blank=True, null=True)
    end_data = models.DateField(default=None, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
