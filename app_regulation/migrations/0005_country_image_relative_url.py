# Generated by Django 5.0.7 on 2024-08-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_regulation', '0004_alter_regulation_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='image_relative_url',
            field=models.CharField(default='default.jpg', max_length=255),
        ),
    ]
