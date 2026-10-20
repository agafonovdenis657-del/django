from django.shortcuts import render
from .models import Group
from .models import Student

def index_view(request):
    return render(request, 'journal/index.html')

def contact_view(request):
    return render(request, 'journal/contacts.html')

def about_view(request):
    return render(request, 'journal/about.html')

def student_view(request):

    all_students = Student.objects.all()


    context = {
        'page_title': 'Студенты',
        'student_list': all_students,
    }


    return render(request, 'journal/students.html', context)

def groups_view(request):
    all_groups = Group.objects.all()

    context = {
     'page_title': 'список учебных групп',
     'groups_list': all_groups,
    }
    return render(request, 'journal/groups.html', context)

def group_detail_view(request, group_id):

    group = Group.objects.get(pk=group_id)

    students_in_group = group.students.all()

    context = {
        'group': group,
        'students': students_in_group,
    }
    return render(request, 'journal/group_detail.html', context)


def student_detail_view(request, student_id):

    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
    }

    return render(request, 'journal/student_detail.html', context)