# Generated by Django 2.1.1 on 2020-05-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnooz', '0004_auto_20200506_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmsgs',
            name='msgtype',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='kmsgs',
            name='sender',
            field=models.CharField(default='', max_length=200),
        ),
    ]