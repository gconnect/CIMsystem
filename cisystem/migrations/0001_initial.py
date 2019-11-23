# Generated by Django 2.2.7 on 2019-11-21 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_center', models.CharField(max_length=200)),
                ('certificate_number', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('town_or_village', models.CharField(max_length=200)),
                ('lga', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('entry_no', models.IntegerField()),
                ('fullname', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('place_of_birth', models.CharField(max_length=200)),
                ('town_or_village_of_birth', models.CharField(max_length=200)),
                ('fullname_of_father', models.CharField(max_length=200)),
                ('fullname_of_mother', models.CharField(max_length=200)),
                ('place_of_issue', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('registered_late', models.BooleanField(default=False)),
                ('id_card', models.FileField(blank=True, default=None, null=True, upload_to='uploads')),
                ('amount_paid', models.IntegerField(blank=True, default=None, null=True)),
                ('registered_date', models.DateTimeField(verbose_name='registered date')),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('is_eligible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Eligible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisystem.Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_center', models.CharField(max_length=200)),
                ('town_or_village', models.CharField(max_length=200)),
                ('lga', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('certificate_number', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('fullname', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('cause_of_death', models.CharField(max_length=200)),
                ('date_of_death', models.DateField(max_length=200)),
                ('place_of_death', models.CharField(max_length=200)),
                ('address_of_deceased', models.CharField(max_length=200)),
                ('corpse_deposited_at', models.CharField(max_length=200)),
                ('certified_death_by', models.CharField(max_length=200)),
                ('place_of_issue', models.CharField(max_length=200)),
                ('name_of_registrar', models.CharField(max_length=200)),
                ('date_of_issue', models.DateField(max_length=200)),
                ('name_of_doctor', models.CharField(max_length=200)),
                ('year', models.DateField(verbose_name='year')),
                ('entry_no', models.IntegerField(blank=True, default=None, null=True)),
                ('certificate_of_origin', models.FileField(blank=True, default=None, null=True, upload_to='uploads')),
                ('affidavit', models.FileField(blank=True, default=None, null=True, upload_to='uploads')),
                ('proof_of_death', models.FileField(blank=True, default=None, null=True, upload_to='uploads')),
                ('certificate_required', models.BooleanField(default=False)),
                ('amount_paid', models.IntegerField()),
                ('registered_date', models.DateTimeField(verbose_name='registered date')),
                ('birth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisystem.Birth')),
            ],
        ),
    ]
