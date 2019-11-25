from django.urls import path

from .views import ChartData
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cisystem'
urlpatterns = [
    path('', views.index,  name='index'),
    path('about/', views.about,  name='about'),
    path('login/', views.login,  name='login'),
    path('contact/', views.contact,  name='contact'),
    # path('user_profile/', views.user_profile,  name='user_profile'),
    path('chart_data/', views.chart_data, name='chart-data'),
    path('birth_certificate/', views.birthCertifcateView,  name='birth_certificate'),
    path('user_login/', views.user_login,  name='user_login'),
    path('<int:pk>/', views.userProfileView.as_view(), name='user_profile'),
    # path(r'^logout/$', views.user_logout, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)