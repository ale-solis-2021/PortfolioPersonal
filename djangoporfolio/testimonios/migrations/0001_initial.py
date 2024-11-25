# Generated by Django 5.1.2 on 2024-10-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('testimonio', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='testimonios/fotos/')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]