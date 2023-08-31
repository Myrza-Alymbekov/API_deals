from django.urls import path

from . import views

urlpatterns = [
    path('deals/', views.DealCreateView.as_view(), name='deals'),
]
