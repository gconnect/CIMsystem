from django.contrib import admin
from .models import Birth, Death, Eligible

# Register your models here.
class BirthAdmin(admin.ModelAdmin):
    list_display = ("fullname", "place_of_birth", "date_of_birth", "registered_date")
    readonly_fields = ['entry_no']
    # this adds filter to the date
    list_filter = ['registered_date']
    # THis adds search to the admin
    search_fields = ['age']
    readonly_fields = ['entry_no', 'age', 'certificate_number', 'username', 'password']

admin.site.register(Birth, BirthAdmin)

class DeathAdmin(admin.ModelAdmin):
    list_display = ("fullname", "place_of_death", "cause_of_death", "registered_date")

    # this adds filter to the date
    list_filter = ['registered_date']
    # THis adds search to the admin
    search_fields = ['fullname']
    readonly_fields = ['entry_no', 'certificate_number', 'birth_id']

admin.site.register(Death, DeathAdmin)

# admin.site.site_header = 'Civil Registration System'

class EligibleAdmin(admin.ModelAdmin):
    list_display =["birth_id"]
admin.site.register(Eligible, EligibleAdmin)