# Generated by Django 2.1.1 on 2020-05-13 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rand', '0002_auto_20200513_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rmsgs',
            old_name='msgR',
            new_name='msgr',
        ),
    ]
