from django.db import models


class NameList(models.Model):
	name 			    = models.CharField(max_length=150, default="name")
	verified 			    = models.BooleanField(default=False)
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.name


class BlogPost(models.Model):
	body 			        = models.CharField(max_length=1000, default="body")
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.body



class NumberGuess(models.Model):
	number 			        = models.CharField(max_length=1000, default="number")
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.number