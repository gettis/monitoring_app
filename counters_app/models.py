from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import hashlib
import time

import random

def uniqueid():
	seed = random.getrandbits(32)
    	return seed



class url_hash(models.Model):
	url_hash = models.BigIntegerField(default=uniqueid)
	
@python_2_unicode_compatible
class app_name(models.Model):
	url_hash = models.BigIntegerField(default=0)
	app_name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.app_name

	

@python_2_unicode_compatible
class Counter(models.Model):
	url_hash = models.BigIntegerField(default=0)
	app_name = models.CharField(max_length=100)
	counter_name = models.CharField(max_length=200)
	counter_value = models.IntegerField()
	pub_date = models.DateTimeField()
	
	def __str__(self):
		return self.counter_name


