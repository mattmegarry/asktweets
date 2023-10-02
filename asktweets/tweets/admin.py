from django.contrib import admin, messages
from django.utils.html import format_html, mark_safe
from .models import MP, Party, Tweet, ClaudeAPIKey, ApifyAPIKey
from .scraper import scrape_tweets

@admin.action(description="Scrape the selected MPs' tweets")
def initiate_tweet_scrape(self, request, queryset):
        if ApifyAPIKey.load().value is None:
            self.message_user(
                request,
                "Please enter an Apify API key in the admin panel.",
                messages.ERROR,
            )
            return
        
        MPcount = queryset.count()
        scrape_tweets(request, queryset)
        
        apify_link = format_html('<a href="https://console.apify.com/" target="_blank">Apify</a>')
        
        self.message_user(
            request,
            mark_safe("{} MPs' tweets are being scraped. Click here to monitor the run: {}".format(MPcount, apify_link)),
            messages.SUCCESS,
        )
        

class MPAdmin(admin.ModelAdmin):
    list_display = ('name', 'twitter_handle', 'tweets_last_scraped_days_ago')
    readonly_fields = ('tweets_last_scraped',)
    list_per_page = 700
    search_fields = ('name',)
    ordering = ('name',)
    actions = [initiate_tweet_scrape]

admin.site.register(MP, MPAdmin)
admin.site.register(Party)
admin.site.register(Tweet)
admin.site.register(ClaudeAPIKey)
admin.site.register(ApifyAPIKey)