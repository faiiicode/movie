# Generated by Django 3.2.15 on 2022-09-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imagee',
            field=models.ImageField(default='def', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
