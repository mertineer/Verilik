from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('hizmetler/', views.ServicesPage.as_view(), name="services"),
    path('iletisim/', views.form_name_view, name="contact"),
    path('ekip/',views.TeamPage.as_view(), name="team"),
]
views.form_name_view
