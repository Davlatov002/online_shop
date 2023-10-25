# Generated by Django 4.2.6 on 2023-10-21 18:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Praduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default='no-image.png', null=True, upload_to='')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('start_data', models.DateField(blank=True, null=True)),
                ('end_data', models.DateField(blank=True, null=True)),
                ('category_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]