# Generated by Django 4.1.5 on 2023-01-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0003_alter_sekolah_options_remove_sekolah_hp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sekolah',
            name='NPSN',
            field=models.CharField(default='', max_length=10),
        ),
    ]
