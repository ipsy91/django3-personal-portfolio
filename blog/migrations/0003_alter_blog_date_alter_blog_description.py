# Generated by Django 4.1.2 on 2022-10-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_descriprion_blog_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(),
        ),
    ]