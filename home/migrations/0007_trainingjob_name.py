# Generated by Django 4.1.5 on 2023-10-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_alter_activatedata_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainingjob",
            name="name",
            field=models.CharField(max_length=128, null=True),
        ),
    ]
