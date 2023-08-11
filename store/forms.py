from django import forms
from .models import Department, Purpose, Student, Material


class StudentForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = '__all__'

