from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filtreAge', views.filtre_age_enfant_view, name='filtreAge'),
    path('dashboard', views.dashboard_page, name='dashboard'),
    path('csv', views.export_csv, name='export_csv'),

]
