# Generated by Django 4.0.4 on 2022-05-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_profile_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='previous_work',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
