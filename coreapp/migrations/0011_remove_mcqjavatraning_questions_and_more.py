# Generated by Django 4.1.3 on 2024-02-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0010_alter_mcqjavatraning_correctans_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mcqjavatraning",
            name="Questions",
        ),
        migrations.AddField(
            model_name="mcqjavatraning",
            name="questions",
            field=models.TextField(blank=True, null=True),
        ),
    ]
