# Generated by Django 4.1.7 on 2023-06-01 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='date_sortie',
            new_name='date_parution',
        ),
    ]
