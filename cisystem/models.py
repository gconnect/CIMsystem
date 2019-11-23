from django.db import models

# Create your models here.


class Birth(models.Model):
    registration_center = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200, default=None, blank=True, null=True)
    town_or_village = models.CharField(max_length=200)
    lga = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    entry_no = models.IntegerField(default=None, blank=True, null=True)
    fullname = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    date_of_birth = models.DateField('date of birth')
    place_of_birth = models.CharField(max_length=200)
    town_or_village_of_birth = models.CharField(max_length=200)
    fullname_of_father = models.CharField(max_length=200)
    fullname_of_mother = models.CharField(max_length=200)
    place_of_issue = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default=None, blank=True, null=True)
    password = models.CharField(max_length=200, default=None, blank=True, null=True)
    registered_late = models.BooleanField(default=False)
    id_card = models.FileField(upload_to='uploads', default=None, blank=True, null=True)
    amount_paid = models.IntegerField( default=None, blank=True, null=True)
    registered_date = models.DateTimeField('registered date')
    age = models.IntegerField(default=None, blank=True, null=True)
    is_eligible = models.BooleanField(default=False)


    def __str__(self):
        return self.fullname

class Death(models.Model):
    birth_id = models.ForeignKey(Birth, on_delete=models.CASCADE, default=None, blank=True, null=True)
    registration_center = models.CharField(max_length=200)
    town_or_village = models.CharField(max_length=200)
    lga = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200, default=None, blank=True, null=True)
    fullname = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    cause_of_death = models.CharField(max_length=200)
    date_of_death = models.DateField(max_length=200)
    place_of_death = models.CharField(max_length=200)
    address_of_deceased = models.CharField(max_length=200)
    corpse_deposited_at = models.CharField(max_length=200)
    certified_death_by = models.CharField(max_length=200)
    place_of_issue = models.CharField(max_length=200)
    name_of_registrar = models.CharField(max_length=200)
    date_of_issue = models.DateField(max_length=200)
    name_of_doctor = models.CharField(max_length=200)
    entry_no = models.IntegerField(default=None, blank=True, null=True)
    certificate_of_origin = models.FileField(upload_to='uploads', default=None, blank=True, null=True)
    affidavit = models.FileField(upload_to='uploads', default=None, blank=True, null=True)
    proof_of_death = models.FileField(upload_to='uploads', default=None, blank=True, null=True)
    certificate_required = models.BooleanField(default=False)
    amount_paid = models.IntegerField()
    registered_date = models.DateTimeField('registered date')

    def __str__(self):
        return self.fullname

class Eligible(models.Model):
    birth_id = models.ForeignKey(Birth, on_delete=models.CASCADE)

    def __int__(self):
        return self.birth_id