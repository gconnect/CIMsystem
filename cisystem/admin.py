from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
import json
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.urls import path

from .models import Birth, Death, Eligible

# Register your models here.
class BirthAdmin(admin.ModelAdmin):
    list_display = ("fullname", "place_of_birth", "date_of_birth", "registered_date", "age", "is_eligible")
    readonly_fields = ['entry_no']
    # this adds filter to the date
    list_filter = ['registered_date']
    # THis adds search to the admin
    search_fields = ['age']
    readonly_fields = ['entry_no', 'age', 'certificate_number', 'username', 'password', 'is_eligible']
    change_form_template = ["admin/change_form.html", "admin/change_list.html"]
    # js = ('admin/js/change_form.js')

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Birth.objects.annotate(date=TruncDay("registered_date"))
                .values("state")
                .annotate(y=Count("id"))
                .order_by("registered_date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
admin.site.register(Birth, BirthAdmin)

class DeathAdmin(admin.ModelAdmin):
    model = Death
    fields = ("fullname", "place_of_death", "cause_of_death", "registered_date")
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
    Birth.objects.filter(is_eligible=True, age__gte=17).count()


admin.site.register(Eligible, EligibleAdmin)