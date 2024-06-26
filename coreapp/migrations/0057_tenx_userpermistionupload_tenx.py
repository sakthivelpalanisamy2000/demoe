# Generated by Django 4.1.3 on 2024-04-11 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0056_alter_userpermistionuploademployee_aptitude_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TenX",
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
                ("programming", models.TextField()),
                ("main", models.TextField()),
            ],
            options={
                "db_table": "tenX",
            },
        ),
        migrations.AddField(
            model_name="userpermistionupload",
            name="tenx",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coreapp.tenx",
            ),
        ),
    ]
