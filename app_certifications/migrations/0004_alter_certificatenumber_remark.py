# Generated by Django 5.1.1 on 2024-09-16 01:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_certifications', '0003_alter_certificatenumber_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatenumber',
            name='remark',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500000, null=True),
        ),
    ]
