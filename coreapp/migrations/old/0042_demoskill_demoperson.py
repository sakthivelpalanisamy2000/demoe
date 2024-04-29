# Generated by Django 4.1.3 on 2024-03-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0041_cpponetitlepractices_cpponetitletestcase_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Demoskill",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Demoperson",
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
                (
                    "skills",
                    models.ManyToManyField(
                        blank=True, null=True, to="coreapp.demoskill"
                    ),
                ),
            ],
        ),
    ]