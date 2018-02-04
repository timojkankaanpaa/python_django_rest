# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

		# Create your models here.
class Country(models.Model):
	id = models.AutoField(primary_key=True)
	code = models.CharField(max_length=3)
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
		
# Create your models here.
class City(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	countryid = models.ForeignKey(Country, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
		
class Customer(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	cityid = models.ForeignKey(City, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name