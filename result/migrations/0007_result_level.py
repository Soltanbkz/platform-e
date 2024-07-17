# Generated by Django 5.0.6 on 2024-07-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0006_remove_result_level"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="level",
            field=models.CharField(
                choices=[("Bachloar", "Bachloar Degree"), ("Master", "Master Degree")],
                max_length=25,
                null=True,
            ),
        ),
    ]