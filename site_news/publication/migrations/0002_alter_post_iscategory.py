# Generated by Django 4.1.4 on 2022-12-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='isCategory',
            field=models.ManyToManyField(default='Без категории', through='publication.PostCategory', to='publication.category'),
        ),
    ]