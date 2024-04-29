# Generated by Django 4.1.3 on 2024-04-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0055_userpermistionuploademployee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="aptitude",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="c",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="cpp",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="english",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="intership",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="java",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="job",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="pd",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="python",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="userpermistionuploademployee",
            name="workshop",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]