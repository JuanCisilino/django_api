# Generated by Django 4.1.5 on 2023-01-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=2)),
                ('stock', models.IntegerField()),
                ('image', models.TextField()),
                ('company', models.CharField(max_length=30)),
                ('isActive', models.BooleanField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('rol', models.CharField(max_length=30)),
                ('carrito', models.TextField()),
                ('empresa', models.CharField(max_length=30)),
            ],
        ),
    ]
