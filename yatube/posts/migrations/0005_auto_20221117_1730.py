# Generated by Django 2.2.16 on 2022-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221111_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Введите текст поста', verbose_name='Текст поста'),
        ),
    ]