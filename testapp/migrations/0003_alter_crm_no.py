# Generated by Django 4.2.5 on 2024-01-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_crm_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm',
            name='no',
            field=models.IntegerField(default=True),
        ),
    ]