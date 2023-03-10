# Generated by Django 4.1.5 on 2023-01-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sekolah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('web', models.CharField(blank=True, max_length=100, null=True)),
                ('hp', models.CharField(max_length=20)),
                ('alamat', models.TextField(max_length=100)),
                ('jenis_sekolah', models.CharField(choices=[('S', 'SMK'), ('U', 'Universitas')], max_length=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
