from django.contrib import admin

from .models import MP, Party, Tweet, ClaudeAPIKey, ApifyAPIKey

class MPAdmin(admin.ModelAdmin):
    list_display = ('name', 'twitter_handle', 'tweets_last_scraped_days_ago')
    readonly_fields = ('tweets_last_scraped',)
    list_per_page = 700
    search_fields = ('name',)

admin.site.register(MP, MPAdmin)
admin.site.register(Party)
admin.site.register(Tweet)
admin.site.register(ClaudeAPIKey)
admin.site.register(ApifyAPIKey)