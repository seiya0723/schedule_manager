from django.urls import path
from . import views

app_name    = "scheduler"
urlpatterns = [ 
    path("", views.index, name="index"),
    path("calendar/<int:pk>/", views.calendar, name="calendar"),


]

