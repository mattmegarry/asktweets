# Generated by Django 4.2.5 on 2023-09-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_alter_mp_options_alter_party_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mp',
            name='constituency',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='mp',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
