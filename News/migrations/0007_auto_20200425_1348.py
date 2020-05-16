# Generated by Django 3.0.5 on 2020-04-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20200425_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'permissions': (('can_see_author', 'Можно видеть автора комментария.'),), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
