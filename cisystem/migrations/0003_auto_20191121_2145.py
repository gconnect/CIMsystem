# Generated by Django 2.2.7 on 2019-11-21 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cisystem', '0002_auto_20191121_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='death',
            name='birth_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cisystem.Birth'),
        ),
    ]
