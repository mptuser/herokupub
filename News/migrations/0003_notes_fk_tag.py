# Generated by Django 3.0.5 on 2020-04-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20200418_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='fk_tag',
            field=models.ManyToManyField(to='News.Tags'),
        ),
    ]