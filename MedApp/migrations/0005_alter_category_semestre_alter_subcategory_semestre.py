# Generated by Django 5.0.7 on 2024-08-31 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedApp', '0004_category_semestre_subcategory_semestre'),
        ('dashboard', '0003_alter_profile_approved_alter_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.semestre'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='semestre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.semestre'),
        ),
    ]