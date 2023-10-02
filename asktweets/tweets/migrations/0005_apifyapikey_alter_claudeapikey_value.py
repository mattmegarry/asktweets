# Generated by Django 4.2.5 on 2023-10-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_claudeapikey_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApifyAPIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default=None, max_length=1000, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Apify API Key',
                'verbose_name_plural': 'Apify API Key',
            },
        ),
        migrations.AlterField(
            model_name='claudeapikey',
            name='value',
            field=models.CharField(default=None, max_length=1000, null=True, unique=True),
        ),
    ]