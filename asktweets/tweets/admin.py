from django.contrib import admin, messages
from django.utils.html import format_html, mark_safe
from .models import MP, Party, Tweet, ClaudeAPIKey, ApifyAPIKey
from .scraper import start_scraper_run
from django.db.models import Q

@admin.action(description="Scrape the selected MPs' tweets")
def initiate_tweet_scrape(self, request, queryset):
        print(type(self))
        errors = False
        if ApifyAPIKey.load().value is None:
            self.message_user(
                request,
                "Please enter an Apify API key in the admin panel.",
                messages.ERROR,
            )
            errors = True
        
        any_twitter_handle_null = queryset.filter(Q(**{'twitter_handle__isnull': True}) | Q(**{'twitter_handle':''})).exists()
        if any_twitter_handle_null:
            self.message_user(
                request,
                "One or more of the selected MPs does not have a Twitter handle.",
                messages.ERROR,
            )
            errors = True
        
        if errors:
            return

        MPcount = queryset.count()
        start_scraper_run(request, queryset)
        
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