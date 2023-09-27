import os
import django
from django.conf import settings

import sys
sys.path.append('../asktweets') 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asktweets.settings')
django.setup()

from tweets.models import MP, Party

conservative = Party.objects.create(name="Conservative") 
labour = Party.objects.create(name="Labour")

MP.objects.create(name="John Doelll", party=conservative)
MP.objects.create(name="Jane Doepppp", party=labour)

print("Created parties and sample MPs")

