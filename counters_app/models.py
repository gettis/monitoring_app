from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Counter(models.Model):
	counter_name = models.CharField(max_length=200)
	counter_value = models.IntegerField()
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.counter_name


