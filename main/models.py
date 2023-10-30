from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Product(models.Model):
    text = models.CharField(max_length=100)
    exp_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()



