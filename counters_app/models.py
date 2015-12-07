from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class Dictionary(models.Model):
    dict_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.dict_name

    #get length of dictionary
    def len(self):
        return Dictionary.objects.count()
    
    #increment a counter. Create a counter if it doesn't exist
    def increment(self, counter_name):
        try:
            entry = Dictionary.objects.get(counter_name=counter_name)
        except:
            Counter.create(dict_entry=self, counter_name=counter_name, counter_value=0)
            return

        updated_count = entry.counter_value + 1
        entry.update(counter_value=updated_count) 

    #get value of counter
    def get(self,counter_name):
        
        try:
            entry = Dictionary.objects.get(counter_name=counter_name)
        except:
            return -1

        return entry.counter_value

    #check if dictionary has a counter
    def contains(self, counter_name):
        if Dictionary.objects.filter(counter_name=counter_name).exists():
            return True
        else:
            return False

    #clear everything
    def clear(self):
        Dictionary.objects.all().delete()

@python_2_unicode_compatible
class Counter(models.Model):
    
    dict_entry = models.ForeignKey(Dictionary)

    counter_name = models.CharField(max_length=200)
    counter_value = models.BigIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.counter_name

