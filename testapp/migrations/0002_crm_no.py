# Generated by Django 4.2.5 on 2024-01-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm',
            name='no',
            field=models.IntegerField(default=False),
        ),
    ]
