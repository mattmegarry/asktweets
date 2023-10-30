from django.contrib import admin, messages
from .models import ApifyAPIKey
from apify_client import ApifyClient

def start_scraper_run(request, MPqueryset):
    print(MPqueryset)

    token=ApifyAPIKey.load().value
    client = ApifyClient(token)

    run_input = {
        "max_tweets": 5,
        "language": "any",
        "collect_user_info": False,
        "use_experimental_scraper": False,
        "user_info": "user info and replying info",
        "max_attempts": 5,
        "from_user": [
        "tomorrowsmps"
        ],
    }

    run = client.actor("shanes~tweet-flash-plus").start(run_input=run_input)
    print(run)

def get_run_data(run_id):
    token=ApifyAPIKey.load().value
    client = ApifyClient(token)
    run = client.run(run_id)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)