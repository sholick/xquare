# Generated by Django 2.1.5 on 2019-03-09 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('ID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField(default='Default Description goes here. Default Description goes here. Default Description goes here. Default Description goes here.')),
                ('Price', models.BigIntegerField()),
                ('Image', models.CharField(default='../../static/images/games/5.jpg', max_length=200)),
                ('Feature', models.BooleanField(default=True)),
                ('Listdate', models.DateField(default=datetime.date(2019, 3, 9))),
            ],
        ),
    ]
