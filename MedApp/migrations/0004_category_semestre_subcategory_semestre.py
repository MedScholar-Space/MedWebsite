# Generated by Django 5.0.7 on 2024-08-31 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0003_subcategory_category'),
        ('dashboard', '0003_alter_profile_approved_alter_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='semestre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.semestre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='semestre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.semestre'),
            preserve_default=False,
        ),
    ]