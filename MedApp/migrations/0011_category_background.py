# Generated by Django 5.0.7 on 2024-09-29 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background',
            field=models.TextField(choices=[('card__orange', 'orange')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]