from django.urls import path
from . import views

app_name = "crudapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('Student_form', views.student_form, name="student_form"),
]
