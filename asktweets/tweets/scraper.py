from django.contrib import admin, messages
from .models import ApifyAPIKey

def scrape_tweets(request, MPqueryset):
    print(MPqueryset)
    from apify_client import ApifyClient

    # Initialize the ApifyClient with your API token
    client = ApifyClient("<YOUR_API_TOKEN>")

    # Prepare the Actor input
    run_input = {
        "max_tweets": 500,
        "language": "any",
        "collect_user_info": False,
        "use_experimental_scraper": False,
        "user_info": "user info and replying info",
        "max_attempts": 5,
    }

    # Run the Actor and wait for it to finish
    run = client.actor("44jFjuTNajCxx2PrD/3ZnxsHgu9XSzTgDcu").call(run_input=run_input)

    # Run the Actor asynchronously
    

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)