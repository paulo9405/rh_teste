# Generated by Django 3.1.1 on 2021-11-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211109_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='legal_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
