# Generated by Django 2.1.1 on 2018-09-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=1, max_length=80, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
