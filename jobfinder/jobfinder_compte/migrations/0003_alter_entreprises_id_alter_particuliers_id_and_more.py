# Generated by Django 4.2 on 2024-10-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinder_compte', '0002_auto_20241016_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprises',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='particuliers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
