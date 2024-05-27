# Generated by Django 5.0 on 2024-05-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
