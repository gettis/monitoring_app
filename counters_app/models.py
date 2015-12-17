from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import hashlib


def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]




@python_2_unicode_compatible
class url_hash(models.Model):
	url_hash = models.CharField(max_length=100,default=_createHash,unique=True)
	def __str__(self):
		return self.url_hash
	

	
@python_2_unicode_compatible
class app_name(models.Model):
	url_hash = models.ForeignKey(url_hash)
	app_name = models.CharField(max_length=200)
	def __str__(self):
		return self.app_name

@python_2_unicode_compatible
class Counter(models.Model):
	app_name = models.ForeignKey(app_name)
	counter_name = models.CharField(max_length=200)
	counter_value = models.IntegerField()
	pub_date = models.DateTimeField()
	
	def __str__(self):
		return self.counter_name


