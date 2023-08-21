# Generated by Django 4.2.1 on 2023-08-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alltreescount'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompaniesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='companies/img')),
                ('treeCount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('offsetCO2', models.DecimalField(decimal_places=4, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects/img')),
                ('required', models.DecimalField(decimal_places=3, max_digits=15)),
                ('funded', models.DecimalField(decimal_places=3, max_digits=15)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sponsorsCount', models.IntegerField()),
            ],
        ),
    ]
