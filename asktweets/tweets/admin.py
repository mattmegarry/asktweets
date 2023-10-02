from django.contrib import admin, messages
from django.utils.html import format_html, mark_safe
from .models import MP, Party, Tweet, ClaudeAPIKey, ApifyAPIKey

@admin.action(description="Log these MPs' names")
def log_name(self, request, queryset):
        MPcount = queryset.count()
        for mp in queryset:
            print(mp.name)
        
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
    actions = [log_name]

admin.site.register(MP, MPAdmin)
admin.site.register(Party)
admin.site.register(Tweet)
admin.site.register(ClaudeAPIKey)
admin.site.register(ApifyAPIKey)