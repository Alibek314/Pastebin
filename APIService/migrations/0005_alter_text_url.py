# Generated by Django 4.2.5 on 2023-10-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIService', '0004_text_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='url',
            field=models.URLField(default='', unique=True),
        ),
    ]