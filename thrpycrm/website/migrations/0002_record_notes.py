# Generated by Django 4.2.9 on 2024-11-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
