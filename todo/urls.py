
from django.urls import path
from .views import todo_list_create

urlpatterns = [
   path("list_create/", todo_list_create)
]
