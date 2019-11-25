from pyexpat.errors import messages

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, JsonResponse
# Create your views here.

from .models import Birth, Death


def index(request):
   return render(request, 'cisystem/index.html')


def about(request):
   return render(request, 'cisystem/about.html')


def login(request):
   return render(request, 'cisystem/login.html')


def contact(request):
   return render(request, 'cisystem/contact.html')

def user_error_login(request):
   return render(request, 'cisystem/user_error_login.html')

class userProfileView(generic.DetailView):
    model = Birth
    template_name = 'brochure/user_profile.html'

def print_certificate(self, request, obj):
        if "print" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.registered_late = False
            obj.save()
            self.message_user(request, "Print certificate")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


def birthCertifcateView(request):
   birth_id = Birth
   template_name = 'cisystem/birth_certificate.html'
   return render(request, template_name, {'birth': birth_id})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            obj = Birth.objects.get(username=username, password=password)
            return render(request, 'cisystem/user_profile.html', {'obj': obj})
    except:
        return render(request, 'cisystem/user_error_login.html')

        # return render(request, 'cisystem/user_error_login.html')



def chart_data(request):
    dataset = Birth.objects \
        .values('age') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('age')

    port_display_name = dict()
    for port_tuple in Birth.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }
    return JsonResponse(chart)


