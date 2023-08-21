# Generated by Django 4.2.1 on 2023-08-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_companieslist_companywebsite_companieslist_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='citizen/')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='CompaniesList',
            new_name='Companies',
        ),
        migrations.RenameModel(
            old_name='ProjectList',
            new_name='Project',
        ),
    ]
