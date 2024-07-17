# Generated by Django 5.0.6 on 2024-07-04 21:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0012_remove_uploadvideo_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadvideo",
            name="file",
            field=models.FileField(
                default=1,
                help_text="Valid Files: pdf, docx, doc, xls, xlsx, ppt, pptx, zip, rar, 7zip",
                upload_to="course_files/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        [
                            "pdf",
                            "docx",
                            "doc",
                            "xls",
                            "xlsx",
                            "ppt",
                            "pptx",
                            "zip",
                            "rar",
                            "7zip",
                        ]
                    )
                ],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="updated_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="upload_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]