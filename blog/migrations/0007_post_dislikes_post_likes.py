# Generated by Django 4.1.2 on 2022-10-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_category_user_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
