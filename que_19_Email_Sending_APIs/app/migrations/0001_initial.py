# Generated by Django 5.1.6 on 2025-03-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
