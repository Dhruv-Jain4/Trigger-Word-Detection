# Generated by Django 4.1.5 on 2023-10-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_trainingjob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainingjob",
            name="ended_at",
            field=models.DateTimeField(null=True),
        ),
    ]
