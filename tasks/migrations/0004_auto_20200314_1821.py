# Generated by Django 3.0.4 on 2020-03-14 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200314_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]
