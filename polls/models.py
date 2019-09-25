from django.db import models
import datetime

# Create your models here.
# Game class
class Store(models.Model):

	ID = models.BigAutoField(primary_key=True)
	Name = models.CharField(max_length = 200)
	Description = models.TextField(default = "Default Description goes here. Default Description goes here. Default Description goes here. Default Description goes here.")
	Price = models.BigIntegerField()
	Image = models.CharField(max_length = 200,default = "../../static/images/games/5.jpg")
	Feature = models.BooleanField(default=True)
	Listdate = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return "storeID="+str(self.ID)+":price="+str(self.Price)
		
	def get_storeID(self):
		return int(self.ID)
	
	@classmethod
	def create(cls, Name, Description, Price, Image, Feature):
		Store = cls(Name = Name, Description = Description, Price = Price, Image = Image, Feature = Feature)
		return book
