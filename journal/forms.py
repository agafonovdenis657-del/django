from django import forms

from .models import Group,Student

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'group']