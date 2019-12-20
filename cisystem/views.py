from re import template

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect, render_to_response
from django.urls import reverse
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Birth, Death


def index(request):
   return render(request, 'cisystem/index.html')

def about(request):
   return render(request, 'cisystem/about.html')

def login(request):
   return render(request, 'cisystem/login.html')

def contact(request):
   return render(request, 'cisystem/contact.html')

def birth_detail(request):
   return render(request, 'cisystem/birth_detail.html')

def death_detail(request):
   return render(request, 'cisystem/death_detail.html')

def late_registration(request):
   return render(request, 'cisystem/late_registration_detail.html')

def death_certificate(request):
    return render(request, 'cisystem/death_certificate.html')

def birth_certificate(request):
    return render(request, 'cisystem/birth_certificate.html')

def user_error_login(request):
   return render(request, 'cisystem/user_error_login.html')

class userProfileView(generic.DetailView):
    model = Birth
    template_name = 'cisystem/user_profile.html'

class birthcertificateView(generic.DetailView):
    model = Birth
    template_name = 'cisystem/birth_certificate.html'

class deathCertificateView(generic.DetailView):
    model = Death
    template_name = 'cisystem/death_certifcate.html'

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    type = request.POST.get('type')
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        if type == 'birth':
            obj = Birth.objects.get(username=username, password=password)
            context = {'obj': obj}
            return render(request, 'cisystem/birth_certificate.html', context)

        else:
            death_obj = Death.objects.get(username=username, password=password)
            return render(request, 'cisystem/death_certificate.html', {'death_obj': death_obj})
    except:
        return render(request, 'cisystem/user_error_login.html')


class get_eligible_listView(generic.ListView):
    template_name = 'cisystem/eligible_list.html'
    context_object_name = 'eligible_list'

    def get_queryset(self):
        return Birth.objects.filter(is_eligible=True, child_age__gte=18)

class get_vital_statistics_View(generic.ListView):
    template_name = 'cisystem/vital_statistics.html'
    context_object_name = 'statistics'

    def get_queryset(self):
        return Birth.objects.all()

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        birth = Birth.objects.all().count()
        death = Death.objects.all().count()
        is_eligible = Birth.objects.filter(is_eligible=True).count()
        total_population = Birth.objects.all().count() - Death.objects.all().count()
        aged_population = Birth.objects.filter(is_eligible=True, child_age__gte=70).count()
        under_aged_population = Birth.objects.filter(is_eligible=True, child_age__lte=18).count()

        labels = ["All birth", "Eligible Voter", "Death", "Total Population", "Aged 70+", "Under Aged below 18"]
        default_items = [birth, is_eligible, death, total_population, aged_population, under_aged_population]
        is_eligible = [is_eligible]
        data = {
                "labels": labels,
                "default": default_items,
                "is_eligible": is_eligible,
        }
        return Response(data)

