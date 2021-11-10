# Generated by Django 3.1.1 on 2021-11-09 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211109_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='admin',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.company'),
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
