# Generated by Django 3.0.7 on 2024-10-16 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobfinder_app', '0003_auto_20241016_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonces',
            name='entreprise',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]