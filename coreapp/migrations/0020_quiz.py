# Generated by Django 4.1.3 on 2024-03-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0019_titleclick_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=500)),
                ("option1", models.CharField(max_length=20)),
                ("option2", models.CharField(max_length=20)),
                ("option3", models.CharField(max_length=20)),
                ("option4", models.CharField(max_length=20)),
                ("answer", models.CharField(max_length=20)),
            ],
        ),
    ]
