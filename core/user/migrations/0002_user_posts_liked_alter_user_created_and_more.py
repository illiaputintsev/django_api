# Generated by Django 5.0.6 on 2024-07-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_post", "0001_initial"),
        ("core_user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="posts_liked",
            field=models.ManyToManyField(related_name="liked_by", to="core_post.post"),
        ),
        migrations.AlterField(
            model_name="user",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
