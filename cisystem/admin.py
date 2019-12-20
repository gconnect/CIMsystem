from django.conf.urls import url
from django.contrib import admin
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
import json
from django.db.models.functions import TruncDay
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import path, reverse
from django.conf import settings
from django.utils.html import format_html

from .models import Birth, Death

# Register your models here.
class BirthAdmin(admin.ModelAdmin):
    list_display = ("surname_of_child", "other_name_of_child", "place_of_birth", "date_of_birth", "registered_date", "child_age", "is_eligible")
    # this adds filter to the date
    list_filter = ['registered_date']
    # THis adds search to the admin
    search_fields = ['child_age', 'surname_of_child']
    readonly_fields = ['entry_no','certificate_number', 'username', 'password']

    change_form_template = ["admin/change_form.html", "admin/change_list.html"]
    # js = ('admin/js/app.js')


    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('email/', self.email),
        ]
        return my_urls + urls
    def email(request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email_of_father = request.POST.get('email_of_father')
            subject = 'Thank you for registering on the Civil Registration System'
            message = ' Here are your login details ' + username + "\n" + password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_of_father, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('index')
            return render(request, 'cisystem/user_profile.html', {'obj': obj})
        except:
            # messages.error(request, 'Wrong Username or password')
            return render(request, 'cisystem/user_error_login.html')



admin.site.register(Birth, BirthAdmin)

class DeathAdmin(admin.ModelAdmin):
    model = Death
    list_display = ("surname_of_deceased", "othername_of_deceased", "place_of_death", "cause_of_death", "registered_date")
    # this adds filter to the date
    list_filter = ['registered_date']
    # THis adds search to the admin
    search_fields = ['surname_of_deceased']
    readonly_fields = ['entry_no', 'certificate_number', 'username', 'password']
admin.site.register(Death, DeathAdmin)

# admin.site.site_header = 'Civil Registration System'

