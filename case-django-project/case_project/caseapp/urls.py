from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("tour-1/", views.info_page, name="info"),
    path("tour-1/bron/", views.bron_page, name="bron"),
    path("tour-1/bron/payment/", views.after_payment, name="afterpayment"),
]