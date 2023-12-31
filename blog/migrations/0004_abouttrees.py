# Generated by Django 4.2.1 on 2023-08-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_mainpagestatic_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='trees/img/')),
                ('nameLotin', models.CharField(max_length=500)),
                ('height', models.CharField(max_length=300)),
                ('wide', models.CharField(max_length=350)),
                ('growing', models.CharField(max_length=1500)),
                ('fruits', models.CharField(max_length=800)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
