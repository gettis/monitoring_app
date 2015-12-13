#from django.conf import settings
#settings.configure()

import requests
from django.core.management.base import BaseCommand
from counters_app.models import Counter

url = "http://localhost:8000/metrix/"

r = requests.get(url)
content = r.content

list_counters = content.split("<br \>")

for counter in list_counters:
    if counter != "":
        c = counter.split("=")
        d = Counter(counter_name="test124", counter_value= c[1])
    d.save()


