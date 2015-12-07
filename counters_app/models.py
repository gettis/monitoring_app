from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class Dictionary(models.Model):
    dict_name = models.CharField(max_length = 200)
    
    def __str__(self):
        return dict_name

    

@python_2_unicode_compatible
class Counter(models.Model):
    
    dict_entry = models.ForeignKey(Dictionary)

    counter_name = models.CharField(max_length=200)
    counter_value = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.counter_name

