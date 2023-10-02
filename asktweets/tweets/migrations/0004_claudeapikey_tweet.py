# Generated by Django 4.2.5 on 2023-10-02 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_mp_constituency_alter_mp_twitter_handle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaudeAPIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000, unique=True)),
            ],
            options={
                'verbose_name': 'Claude API Key',
                'verbose_name_plural': 'Claude API Key',
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_tweet_id', models.CharField(max_length=255, unique=True)),
                ('tweet_text', models.CharField(max_length=280)),
                ('tweet_date', models.DateTimeField()),
                ('mp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.mp')),
            ],
        ),
    ]
