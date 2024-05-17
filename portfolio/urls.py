from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('mijn_werk/', views.mijn_werk, name='mijn_werk'),
    path('over_mij/', views.over_mij, name='over_mij'),
    path('services/', views.services, name='services'),
    path('werk/<int:id>', views.werk_sing, name='solo-work'),
]