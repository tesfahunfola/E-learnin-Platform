# Generated by Django 4.1.13 on 2024-10-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Subject',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='Course',
            new_name='course',
        ),
    ]