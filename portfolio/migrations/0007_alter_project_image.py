# Generated by Django 4.1.2 on 2022-10-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(null=True, upload_to="portfolio/images"),
        ),
    ]
