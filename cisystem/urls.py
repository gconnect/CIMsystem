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
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)