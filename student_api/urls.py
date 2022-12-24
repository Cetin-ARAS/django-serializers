from django.urls import path
from .views import (
    home,
    students_list,
    student_create,
    student_detail
)

urlpatterns = [
    path("", home),
    path("student-list/", students_list, name='list'),
    path("student-create/", student_create, name='create'),
    path("student_detail/<int:pk>", student_detail, name='detail'),
]