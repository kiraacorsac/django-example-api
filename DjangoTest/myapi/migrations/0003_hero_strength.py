# Generated by Django 4.0.4 on 2022-05-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='strength',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
