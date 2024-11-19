from django.db import models


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=0) #cents

	def __str__(self):
		return self.name


class SubscriptionProduct(Product):
	subscription_duration = models.IntegerField(default=0) #0 - 1 month, 1 - 1 year
