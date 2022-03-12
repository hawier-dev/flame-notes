from django.urls import path
from .views import dashboard, delete_post

app_name = "flame_notes"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('delete/<post_id>',delete_post,name='delete')
]
