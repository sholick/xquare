# Generated by Django 2.1.5 on 2019-03-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='Listdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
