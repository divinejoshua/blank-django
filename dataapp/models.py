from django.db import models


class NameList(models.Model):
	name 			        = models.CharField(max_length=150, default="name")
	department 			        = models.CharField(max_length=150, default="department")
	level 			        = models.CharField(max_length=150, default="level")
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.name


class Visitors(models.Model):
	name 			        = models.CharField(max_length=150, default="visitor")
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.name



class NameListCheck(models.Model):
	name 			        = models.CharField(max_length=150, default="check")
	time         			= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.name