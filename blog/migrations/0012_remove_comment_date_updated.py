# Generated by Django 3.2.4 on 2021-08-10 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210810_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_updated',
        ),
    ]