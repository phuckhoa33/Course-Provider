# Generated by Django 4.2.4 on 2024-01-05 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
