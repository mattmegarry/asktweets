import os
import django
from django.conf import settings
import csv
import sys

# This script is intended to be run on an empty database #

sys.path.append('../asktweets') 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asktweets.settings')
os.environ['DJANGO_DEBUG'] = "true"
django.setup()

from tweets.models import MP, Party

parties = []

with open('scripts/mps.csv') as csvfile:  
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        if row[headers.index('Party')] not in parties:
            party = row[headers.index('Party')]
            parties.append(party)
            Party.objects.create(name=party)

        name = row[headers.index('Name')]
        party = Party.objects.get(name=row[headers.index('Party')])
        constituency = row[headers.index('Constituency')]
        twitter_handle = row[headers.index('Twitter Handle')]
        if name.startswith('Mr ') or name.startswith('Ms '):
            name = name[3:]
        if name.startswith('Mrs ') or name.startswith('Sir '):
            name = name[4:]
        if twitter_handle.startswith('https://twitter.com/'):
            twitter_handle = twitter_handle[20:]
            
        MP.objects.create(name=name, party=party, constituency=constituency, twitter_handle=twitter_handle)

print("Script finished running.")


