# Generated by Django 2.1.1 on 2018-10-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20181021_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]