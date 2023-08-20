from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:url>", view=views.redirect_site, name="redirect_site"),
]
