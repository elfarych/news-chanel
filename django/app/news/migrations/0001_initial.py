# Generated by Django 4.1 on 2022-08-29 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('rank', models.PositiveSmallIntegerField(null=True)),
                ('symbol', models.CharField(max_length=15, null=True)),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('event_date', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('proof', models.CharField(max_length=255, null=True)),
                ('source', models.CharField(max_length=255, null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='events', to='news.category')),
                ('coin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='news.coin')),
            ],
            options={
                'ordering': ('-event_date',),
            },
        ),
    ]