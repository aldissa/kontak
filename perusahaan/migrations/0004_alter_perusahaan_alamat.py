# Generated by Django 4.1.5 on 2023-01-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0003_remove_perusahaan_web_perusahaan_bidang_perusahaan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perusahaan',
            name='Alamat',
            field=models.TextField(max_length=20),
        ),
    ]
