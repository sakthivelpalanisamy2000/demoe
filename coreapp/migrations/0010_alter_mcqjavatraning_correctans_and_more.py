# Generated by Django 4.1.3 on 2024-02-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0009_mcqjavatraning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mcqjavatraning",
            name="correctans",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mcqjavatraning",
            name="optiona",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mcqjavatraning",
            name="optionb",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mcqjavatraning",
            name="optionc",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mcqjavatraning",
            name="optiond",
            field=models.TextField(blank=True, null=True),
        ),
    ]
