from django.contrib import admin, messages
from apify_client import ApifyClient
import requests
import json

import os
import dotenv
dotenv.load_dotenv()

APIFY_API_KEY=os.environ.get("APIFY_API_KEY")

def start_scraper_run():
    client = ApifyClient(APIFY_API_KEY)

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
    # get the run data with raw requests
    url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={APIFY_API_KEY}"
    print(url)
    response = requests.get(url)
    # iterate over the items in the dataset
    print(response.json())
    dataset_id = response.json()["data"]["defaultDatasetId"]
    print(dataset_id)
    url2 = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={APIFY_API_KEY}"
    print(url2)
    response2 = requests.get(url2)
    print(response2.json())
    return response2.json()

#start_scraper_run()
get_run_data("Q0ZhYDdmqUivCnaLs")