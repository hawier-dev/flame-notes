# Generated by Django 4.0.2 on 2022-03-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
