# Generated by Django 4.1.3 on 2024-03-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0043_pythontraingclick_cpptraingclick"),
    ]

    operations = [
        migrations.AddField(
            model_name="ctraingtitle",
            name="mcqscore",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="ctraingtitle",
            name="mcqtotal",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="ctraingtitle",
            name="test",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
