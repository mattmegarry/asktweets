from django.db import models
from django.utils import timezone

class Party(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Parties"

    def __str__(self):
        return self.name

class MP(models.Model):
    name = models.CharField(max_length=600, blank=False, null=False)
    party = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)
    constituency = models.CharField(max_length=600, null=True, blank=True)
    twitter_handle = models.CharField(max_length=255, null=True, blank=True)
    tweets_last_scraped = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = "MPs"

    def __str__(self):
        return self.name
    
    def tweets_last_scraped_days_ago(self):
        now = timezone.now()
        if self.tweets_last_scraped is None:
            return None
        delta = now - self.tweets_last_scraped
        return delta.days
    
class Tweet(models.Model):
    twitter_tweet_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    tweet_text = models.CharField(max_length=280, blank=False, null=False)
    tweet_date = models.DateTimeField(blank=False, null=False)
    mp = models.ForeignKey(MP, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tweet_text[:50]

class ClaudeAPIKey(models.Model):
    value = models.CharField(max_length=1000, unique=True, blank=False, null=True, default=None)

    class Meta:
        verbose_name = "Claude API Key"
        verbose_name_plural = "Claude API Key"

    def __str__(self):
        return "Claude API Key"

    def save(self, *args, **kwargs):
        self.pk = 1
        self.__class__.objects.exclude(pk=1).delete()
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
class ApifyAPIKey(models.Model):
    value = models.CharField(max_length=1000, unique=True, blank=False, null=True, default=None)

    class Meta:
        verbose_name = "Apify API Key"
        verbose_name_plural = "Apify API Key"

    def __str__(self):
        return "Apify API Key"

    def save(self, *args, **kwargs):
        self.pk = 1
        self.__class__.objects.exclude(pk=1).delete()
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    

