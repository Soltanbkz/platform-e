# Generated by Django 5.0.6 on 2024-07-16 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0032_remove_program_thumbnail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courseallocation",
            name="program",
        ),
    ]