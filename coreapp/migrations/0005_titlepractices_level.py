# Generated by Django 4.1.3 on 2024-02-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0004_titlepractices_alter_questionpractices_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="titlepractices",
            name="level",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
