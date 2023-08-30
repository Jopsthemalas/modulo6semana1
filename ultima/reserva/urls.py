from django.urls import path

from reserva.views import criar_reserva



urlpatterns = [

    path ('criar/' ,criar_reserva, name = "criar_reserva"),
]