# Generated by Django 5.0.6 on 2024-07-11 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0005_alter_result_id_alter_takencourse_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="level",
        ),
    ]