# Generated by Django 4.1.6 on 2023-03-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='picture',
            field=models.ImageField(default='pictures/2023/02/sample.jpg', upload_to='pictures/%Y/%m'),
        ),
    ]
