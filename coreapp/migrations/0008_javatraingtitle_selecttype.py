# Generated by Django 4.1.3 on 2024-02-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0007_javatraingtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="javatraingtitle",
            name="selecttype",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
