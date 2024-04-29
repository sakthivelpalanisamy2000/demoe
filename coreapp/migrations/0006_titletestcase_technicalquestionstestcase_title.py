# Generated by Django 4.1.3 on 2024-02-19 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0005_titlepractices_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="Titletestcase",
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
                ("title", models.CharField(blank=True, max_length=1000, null=True)),
                ("level", models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="technicalquestionstestcase",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coreapp.titletestcase",
            ),
        ),
    ]