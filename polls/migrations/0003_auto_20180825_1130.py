# Generated by Django 2.1 on 2018-08-25 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180825_1122'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='choice',
            table='Choice',
        ),
        migrations.AlterModelTable(
            name='question',
            table='Question',
        ),
    ]
