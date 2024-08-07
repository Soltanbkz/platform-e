# Generated by Django 5.0.6 on 2024-07-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0010_alter_question_figure"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="figure",
            field=models.ImageField(
                blank=True,
                default="default.png",
                help_text="Add an image for the question if it's necessary.",
                null=True,
                upload_to="figure_pictures/",
                verbose_name="Figure",
            ),
        ),
    ]
