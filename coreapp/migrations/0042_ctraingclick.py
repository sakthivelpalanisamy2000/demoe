# Generated by Django 4.1.3 on 2024-03-22 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("coreapp", "0041_cpponetitlepractices_cpponetitletestcase_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ctraingclick",
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
                ("click", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Cuserclick",
            },
        ),
    ]