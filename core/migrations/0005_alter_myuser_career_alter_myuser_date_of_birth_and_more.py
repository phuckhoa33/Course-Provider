# Generated by Django 4.2.4 on 2024-01-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_myuser_cared_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='career',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='school',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]