# Generated by Django 4.1.5 on 2023-03-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aws_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('aw_access_key', models.CharField(max_length=80)),
                ('aws_secret_access', models.CharField(max_length=100)),
                ('bucket_name', models.CharField(max_length=80)),
                ('bucket_prefix', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]