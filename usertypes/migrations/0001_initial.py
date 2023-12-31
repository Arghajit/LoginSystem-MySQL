# Generated by Django 4.2.7 on 2023-11-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('picture', models.FileField(upload_to='images')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
