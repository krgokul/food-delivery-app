# Generated by Django 4.2.17 on 2025-01-13 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AlterModelTable(
            name="user",
            table="users",
        ),
    ]