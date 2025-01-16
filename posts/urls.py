from django.urls import path
from .views import home_view ,HomePageView, HomePageTemplateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]