# Generated by Django 3.2.9 on 2021-11-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('description', models.TextField(max_length=255)),
                ('company', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=155)),
                ('phone', models.CharField(blank=True, max_length=155)),
                ('email', models.CharField(blank=True, max_length=155)),
                ('icon', models.ImageField(blank=True, upload_to='media/images/setting/')),
                ('facebook', models.CharField(blank=True, max_length=155)),
                ('instagram', models.CharField(blank=True, max_length=155)),
                ('twitter', models.CharField(blank=True, max_length=155)),
                ('youtube', models.URLField()),
                ('aboutus', models.TextField(blank=True)),
                ('contact', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud emas')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
            },
        ),
    ]