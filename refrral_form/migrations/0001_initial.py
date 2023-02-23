# Generated by Django 3.2.7 on 2022-01-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FORM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('DOB', models.DateField(null=True)),
                ('EMAIL', models.EmailField(max_length=254, null=True)),
                ('COURSE', models.CharField(max_length=30)),
                ('YEAR', models.IntegerField()),
                ('CONTACT_NUM', models.IntegerField()),
                ('WHATSAPP', models.IntegerField()),
                ('COLLEGE', models.CharField(max_length=200)),
                ('AREA_OF_HOSTEL', models.CharField(max_length=200)),
            ],
        ),
    ]
