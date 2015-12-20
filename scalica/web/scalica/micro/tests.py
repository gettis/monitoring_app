from django.test import TestCase
from scalica.counters_app.models import Counter

counter = Counter.object.create(counter_name='test_counter')

Counter.objects.values_list('counter_name', flat=True)
