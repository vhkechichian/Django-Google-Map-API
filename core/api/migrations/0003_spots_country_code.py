# Generated by Django 2.2.3 on 2019-07-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='spots',
            name='country_code',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
