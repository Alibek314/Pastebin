# Generated by Django 4.2.5 on 2023-10-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIService', '0003_remove_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]