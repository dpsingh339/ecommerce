# Generated by Django 3.0.6 on 2020-05-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=50)),
                ('Product_Description', models.CharField(max_length=300)),
                ('Category', models.CharField(max_length=50)),
                ('Sub_Category', models.CharField(max_length=50)),
                ('Publish_Date', models.DateField()),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
