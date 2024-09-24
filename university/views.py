from django.shortcuts import render
from .models import Faculty, Student, Subject, Teacher, Group, Kafedra


def faculty_list(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render (request, 'faculty-list.html', ctx)


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render (request, 'student-list.html', ctx)


def kafedra_list(request):
    kafedra = Kafedra.objects.all()
    ctx = {'kafedra': kafedra}
    return render (request, 'kafedra-list.html', ctx)


def subject_list(request):
    subject = Subject.objects.all()
    ctx = {'subject': subject}
    return render (request, 'subject-list.html', ctx)


def teacher_list(request):
    teacher = Teacher.objects.all()
    ctx = {'teacher': teacher}
    return render (request, 'teacher-list.html', ctx)


def group_list(request):
    group = Group.objects.all()
    ctx = {'group': group}
    return render (request, 'group-list.html', ctx)
