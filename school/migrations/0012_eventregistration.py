# Generated by Django 3.0.5 on 2024-03-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=10)),
            ],
        ),
    ]