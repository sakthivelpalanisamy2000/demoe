# Generated by Django 4.1.3 on 2024-03-20 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0043_demoskill_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cpponetechnicalquestionstestcase",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coreapp.cpponetitletestcase",
            ),
        ),
    ]
