# Generated by Django 4.2.5 on 2023-10-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_apifyapikey_alter_claudeapikey_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='mp',
            name='tweets_last_scraped',
            field=models.DateTimeField(null=True),
        ),
    ]
