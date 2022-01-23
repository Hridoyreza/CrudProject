from django.shortcuts import render

from . import forms

from .  models import Student


def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title': 'Home', "student_list": student_list}
    return render(request, 'index.html', context=diction)


def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Student Form', "student_form": form}
    return render(request, 'Student_form.html', context=diction)
