# Generated by Django 5.0 on 2024-01-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('dep', models.CharField(choices=[('HR', 'Humen Resourse'), ('CS', 'Computer Science'), ('EE', 'Electronic Engineer ')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]