# Generated by Django 2.0.6 on 2018-06-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Ashwin', max_length=150),
            preserve_default=False,
        ),
    ]
