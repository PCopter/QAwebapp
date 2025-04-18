# Generated by Django 5.1.1 on 2024-10-22 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_regulation', '0010_alter_regulation_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeRegulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='regulation',
            name='received_information_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='mandatory_voluntory',
            field=models.CharField(choices=[('Mandatory', 'Mandatory'), ('Voluntary', 'Voluntary'), ('N/A', 'N/A')], max_length=15),
        ),
        migrations.AddField(
            model_name='regulation',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_regulation.typeregulation'),
        ),
    ]
