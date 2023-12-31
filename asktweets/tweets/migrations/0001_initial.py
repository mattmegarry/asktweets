# Generated by Django 4.2.5 on 2023-09-27 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('constituency', models.CharField(max_length=600)),
                ('twitter_handle', models.CharField(max_length=255)),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.party')),
            ],
        ),
    ]
