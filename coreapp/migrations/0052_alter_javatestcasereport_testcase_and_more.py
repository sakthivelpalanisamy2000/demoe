# Generated by Django 4.1.3 on 2024-04-07 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0051_javatestcasereport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="javatestcasereport",
            name="testcase",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coreapp.technicalquestionstestcase",
            ),
        ),
        migrations.AlterField(
            model_name="javatestcasereport",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coreapp.titletestcase",
            ),
        ),
    ]