from django import forms
from django.forms import ModelForm
from .models import Employee, Company, Department


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = [
            'name',
            'user',
            'gender',
            'department',
            'phone',
            'role',
            'age',
            'joining_date',
            'salary',
        ]



