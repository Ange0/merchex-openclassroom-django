# Generated by Django 4.1.3 on 2022-11-10 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('CD', 'Coupe Decaler')], max_length=5)),
                ('biography', models.CharField(max_length=1000)),
                ('year_formed', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1900), django.core.validators.MaxLengthValidator(2021)])),
                ('active', models.BooleanField(default=True)),
                ('official_homepage', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1900), django.core.validators.MaxLengthValidator(2021)])),
                ('type', models.CharField(choices=[('RS', 'Records'), ('CG', 'Clothing'), ('PS', 'Posters'), ('MS', 'Miscellaneous')], max_length=5)),
            ],
        ),
    ]
