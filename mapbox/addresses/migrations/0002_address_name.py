# Generated by Django 4.2.1 on 2023-06-12 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]