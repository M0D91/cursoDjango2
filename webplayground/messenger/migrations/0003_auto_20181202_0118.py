# Generated by Django 2.1.3 on 2018-12-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20181202_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
