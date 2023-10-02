from django.contrib import admin

from .models import MP, Party, Tweet, ClaudeAPIKey, ApifyAPIKey

admin.site.register(MP)
admin.site.register(Party)
admin.site.register(Tweet)
admin.site.register(ClaudeAPIKey)
admin.site.register(ApifyAPIKey)