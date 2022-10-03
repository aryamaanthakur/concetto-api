# Generated by Django 4.1.1 on 2022-10-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workshop",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("summary", models.CharField(max_length=250)),
                ("details", models.TextField()),
                ("register_link", models.URLField()),
                ("image", models.ImageField(upload_to="workshop_images")),
                ("register_timestamp", models.DateTimeField()),
                ("start_timestamp", models.DateTimeField()),
                ("end_timestamp", models.DateTimeField()),
            ],
        ),
    ]