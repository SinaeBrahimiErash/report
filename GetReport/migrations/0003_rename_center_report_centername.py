# Generated by Django 4.0.10 on 2024-05-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GetReport', '0002_alter_report_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='center',
            new_name='centername',
        ),
    ]
