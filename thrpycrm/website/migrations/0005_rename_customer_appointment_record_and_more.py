# Generated by Django 4.2.9 on 2024-11-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='customer',
            new_name='record',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
