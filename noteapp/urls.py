from django.urls import path
from .views import dashboard,create

app_name = "Flame Notes"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("create/", create, name="create")
]
