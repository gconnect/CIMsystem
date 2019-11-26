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
    path('chart_data/', views.chart_data, name='chart-data'),
    path('birth_certificate/', views.get_birth_certificateView.as_view(),  name='birth_certificate'),
    path('user_login/', views.user_login,  name='user_login'),
    path('user_error_login/', views.user_error_login,  name='user_error_login'),
    path('eligible_list/', views.get_eligible_listView.as_view(),  name='eligible_list'),
    path('vital_statistics/', views.get_vital_statistics_View.as_view(),  name='statistics'),
    path('<int:pk>/', views.userProfileView.as_view(), name='user_profile'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)