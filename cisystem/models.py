import uuid
from enum import Enum

from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse_lazy
from model_utils import Choices


class Birth(models.Model):
    registration_center = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200, default=None, blank=True, null=True)
    town_or_village_of_registration = models.CharField(max_length=200)
    LGA_of_registration = models.CharField(max_length=200)
    state_of_registration = models.CharField(max_length=200)
    entry_no = models.IntegerField(default=None,blank=True, null=True)
    surname_of_child = models.CharField(max_length=200)
    other_name_of_child = models.CharField(max_length=200)

    class SEX (Enum):
        male = ('male', 'Male')
        female = ('female', 'Female')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]

    sex = models.CharField(max_length=200, choices=[x.value for x in SEX], default=SEX.get_value('male'),)

    class PLACE (Enum):
        hospital = ('hospital', 'Hospital')
        maternity = ('maternity', 'Maternity')
        church = ('church', 'Church')
        home = ('home', 'Home')
        others = ('others', 'Others')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    place_of_birth = models.CharField(max_length=200, choices=[x.value for x in PLACE], default=PLACE.get_value('hospital'),)
    date_of_birth = models.DateTimeField('date of birth')
    town_or_village_of_birth = models.CharField(max_length=200)

    surname_of_mother = models.CharField(max_length=200)
    Other_name_of_mother = models.CharField(max_length=200)
    residence_of_mother = models.CharField(max_length=200)
    age_of_mother_at_child_birth = models.CharField(max_length=200)
    state_of_origin_of_mother = models.CharField(max_length=200)
    ethnicity_of_mother = models.CharField(max_length=200, default=None, blank=False)

    class MOTHER_STATUS (Enum):
        married = ('married', 'Married')
        divorce = ('divorce', 'Divorce')
        seperate = ('seperate', 'Seperate')
        widow = ('widow', 'Widow')
        single = ('single', 'Single')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    mother_marital_status = models.CharField(max_length=200, choices=[x.value for x in MOTHER_STATUS], default=MOTHER_STATUS.get_value('married'),)

    class MOTHER_NATIONALITY (Enum):
        nigeria = ('nigeria', 'Nigeria')
        others = ('others', 'Others')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    nationality_of_mother = models.CharField(max_length=200, choices=[x.value for x in MOTHER_NATIONALITY], default=MOTHER_NATIONALITY.get_value('nigeria'),)

    occupation_of_mother = models.CharField(max_length=200)
    educational_qualification_of_mother = models.CharField(max_length=200)
    mother_phone = models.CharField(max_length=200, default=None, blank=True)
    mother_email = models.EmailField(max_length=200, default=None, blank=True)

    surname_of_father = models.CharField(max_length=200)
    other_name_of_father = models.CharField(max_length=200)
    state_of_origin_of_father = models.CharField(max_length=200)
    ethnicity_of_father = models.CharField(max_length=200)

    class FATHER_STATUS(Enum):
        married = ('married', 'Married')
        divorce = ('divorce', 'Divorce')
        seperate = ('seperate', 'Seperate')
        widow = ('widow', 'Widow')
        single = ('single', 'Single')

        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    father_marital_status = models.CharField(max_length=200, choices=[x.value for x in FATHER_STATUS], default=FATHER_STATUS.get_value('married'),)

    class FATHER_NATIONALITY (Enum):
        nigeria = ('nigeria', 'Nigeria')
        others = ('others', 'Others')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    nationality_of_father = models.CharField(max_length=200, choices=[x.value for x in FATHER_NATIONALITY], default=FATHER_NATIONALITY.get_value('nigeria'),)
    occupation_of_father = models.CharField(max_length=200)
    educational_qualification_of_father = models.CharField(max_length=200)
    phone_of_father = models.CharField(max_length=200, default=None, blank=True)
    email_of_father = models.EmailField(max_length=200, default=None, blank=True)

    relationship_with_child = models.CharField(max_length=200)
    surname_of_informant = models.CharField(max_length=200)
    other_name_of_informant = models.CharField(max_length=200)
    address_of_informant = models.CharField(max_length=200)
    phone_of_informant = models.CharField(max_length=200, default=None, blank=True)
    email_of_informant = models.CharField(max_length=200, default=None, blank=True)

    username = models.CharField(max_length=200, default=None, blank=True, null=True, unique=True)
    password = models.CharField(max_length=200, default=None, blank=True, null=True)
    registered_late = models.BooleanField(default=False)
    id_card = models.FileField(upload_to='uploads', default=None, blank=True, null=True)
    amount_paid = models.IntegerField(default=None, blank=True, null=True)
    registered_date = models.DateTimeField(auto_now=True)
    child_age = models.IntegerField(default=None, blank=True, null=True)
    place_of_issue = models.CharField(max_length=200,default=None, blank=False, null=False)
    name_of_registrar = models.CharField(max_length=200, default=None, blank=False, null=False)
    is_eligible = models.BooleanField(default=False)
    is_dead = models.BooleanField(default=False)

    def __str__(self):
        return self.surname_of_child

def set_entry_no(sender, instance, **kwargs):
    if not instance.entry_no:
        instance.entry_no = instance.id
    return instance.entry_no
models.signals.pre_save.connect(set_entry_no, sender=Birth)


def set_username(sender, instance, **kwargs):
        if not instance.username:
            username = instance.surname_of_child.replace(" ", "").lower()
            counter = 1
            while Birth.objects.filter(username=username):
                username = instance.surname_of_child + str(counter)
                counter += 1
            instance.username = username
models.signals.pre_save.connect(set_username, sender=Birth)


def random_password(sender, instance, **kwargs):
    if not instance.password:
        instance.password = uuid.uuid4().hex[:8]
models.signals.pre_save.connect(random_password, sender=Birth)


def set_certificate_no(sender, instance, **kwargs):
        if not instance.certificate_number:
          instance.certificate_number = uuid.uuid4().hex[:8].upper()
models.signals.pre_save.connect(set_certificate_no, sender=Birth)


def calculate_age(sender, instance, **kwargs):
    today = date.today()
    if not instance.child_age:
        instance.child_age = today.year - instance.date_of_birth.year - ((today.month, today.day) < (instance.date_of_birth.month, instance.date_of_birth.day))
    return instance.child_age
models.signals.pre_save.connect(calculate_age, sender=Birth)


def check_eligible(sender, instance, **kwargs):
    if not instance.is_eligible:
        instance.is_eligible = calculate_age(check_eligible, instance) > 17
        return instance.is_eligible
    else:
        return False
models.signals.pre_save.connect(check_eligible, sender=Birth)


class Death(models.Model):
    birth_id = models.ForeignKey(Birth, on_delete=models.CASCADE, default=None, blank=True, null=True)
    registration_center = models.CharField(max_length=200)
    town_or_village_of_registration = models.CharField(max_length=200)
    LGA_of_registration = models.CharField(max_length=200)
    state_of_registration = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=200, default=None, blank=True, null=True)

    surname_of_deceased = models.CharField(max_length=200)
    othername_of_deceased = models.CharField(max_length=200)
    class SEX (Enum):
        male = ('male', 'Male')
        female = ('female', 'Female')
        @classmethod
        def get_value(cls, members):
            return cls[members].value[0]
    sex = models.CharField(max_length=200, choices=[x.value for x in SEX], default=SEX.get_value('male'),)
    date_of_death = models.DateField(max_length=200)
    occupation_of_deceased = models.CharField(max_length=200)
    cause_of_death = models.CharField(max_length=200)
    place_of_death = models.CharField(max_length=200)
    residence_of_deceased = models.CharField(max_length=200)
    age_at_death = models.IntegerField()
    surname_of_informant = models.CharField(max_length=200)
    othername_of_informant = models.CharField(max_length=200)
    relationship_to_deceased = models.CharField(max_length=200)
    address_of_informant = models.CharField(max_length=200)
    phone_of_informant = models.CharField(max_length=200, default=None, blank=True)
    email_of_informant = models.EmailField(max_length=200)

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
    username = models.CharField(max_length=200, default=None, blank=True, null=True, unique=True)
    password = models.CharField(max_length=200, default=None, blank=True, null=True)
    registered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surname_of_deceased

def death_certificate_no(sender, instance, **kwargs):
        if not instance.certificate_number:
            instance.certificate_number = uuid.uuid4().hex[:8].upper()
models.signals.pre_save.connect(set_certificate_no, sender=Death)


def death_entry_no(sender, instance, **kwargs):
    if not instance.entry_no:
        instance.entry_no = instance.id
    return instance.entry_no
models.signals.pre_save.connect(set_entry_no, sender=Death)


def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = instance.surname_of_deceased.replace(" ", "").lower()
        counter = 1
        while Death.objects.filter(username=username):
            username = instance.surname_of_deceased + str(counter)
            counter += 1
        instance.username = username


models.signals.pre_save.connect(set_username, sender=Death)


def random_password(sender, instance, **kwargs):
    if not instance.password:
        instance.password = uuid.uuid4().hex[:8]


models.signals.pre_save.connect(random_password, sender=Death)