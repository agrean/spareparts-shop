from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Items(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=4000, default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    created_by = models.ForeignKey(User, null=True, related_name='items')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)


    def __str__(self):
    	return self.name

    class Meta:
        pass