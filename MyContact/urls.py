# MyContact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact1/', views.controleform1, name='controleform1'),  # Chemin pour accéder au formulaire1
    path('contact2/', views.controleform2, name='controleform2'),  # Chemin pour accéder au formulaire2
    path('contact3/', views.controleform3, name='controleform3'),  # Chemin pour accéder au formulaire3

]
