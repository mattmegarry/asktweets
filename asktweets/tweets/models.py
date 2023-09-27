from django.db import models

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

    class Meta:
        verbose_name_plural = "MPs"

    def __str__(self):
        return self.name
