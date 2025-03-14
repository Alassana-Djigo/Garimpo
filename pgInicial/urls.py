from django.urls import path
from . import views

app_name = "pgInicial"

urlpatterns = [
    path("", views.index, name = "index")
]
