# Generated by Django 4.1 on 2022-08-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='text',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
