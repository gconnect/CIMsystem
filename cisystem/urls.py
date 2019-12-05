from django.conf.urls import url
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cisystem'
urlpatterns = [
    path('', views.index,  name='index'),
    path('about/', views.about,  name='about'),
    path('login/', views.login,  name='login'),
    path('contact/', views.contact,  name='contact'),
    path('birth_detail/', views.birth_detail,  name='birth_detail'),
    path('death_detail/', views.death_detail,  name='death_detail'),
    path('late_registration/', views.late_registration,  name='late_registration'),
    path('user_login/', views.user_login,  name='user_login'),
    path('user_error_login/', views.user_error_login,  name='user_error_login'),
    path('eligible_list/', views.get_eligible_listView.as_view(),  name='eligible_list'),
    path('vital_statistics/', views.get_vital_statistics_View.as_view(),  name='statistics'),
    path('<int:pk>/', views.userProfileView.as_view(), name='user_profile'),
    path('<int:pk>/birth_certificate/', views.birthcertificateView.as_view(), name='certificate'),
    path('<int:pk>/death_certificate/', views.deathCertificateView.as_view(), name='death_certificate_view'),
    path('birth_certificate/', views.birth_certificate, name='birth_certificate'),
    path('death_certificate/', views.death_certificate, name='death_certificate'),
    path('api/chart/data/', views.ChartData.as_view(), name='api_data'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)