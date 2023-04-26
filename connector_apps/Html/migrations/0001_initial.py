# Generated by Django 4.1.7 on 2023-03-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Html_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=100)),
                ('flavor', models.CharField(blank=True, max_length=40)),
                ('header', models.CharField(blank=True, max_length=40)),
                ('index_col', models.CharField(blank=True, max_length=40)),
                ('skiprows', models.CharField(blank=True, max_length=40)),
                ('attrs', models.CharField(blank=True, max_length=40)),
                ('parse_dates', models.CharField(blank=True, max_length=40)),
                ('thousands', models.CharField(blank=True, max_length=40)),
                ('encoding', models.CharField(blank=True, max_length=40)),
                ('decimal', models.CharField(blank=True, max_length=40)),
                ('converters', models.CharField(blank=True, max_length=40)),
                ('na_values', models.CharField(blank=True, max_length=40)),
                ('keep_default_na', models.CharField(blank=True, max_length=40)),
                ('displayed_only', models.CharField(blank=True, max_length=40)),
                ('extract_links', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
