from django import forms
from django.forms import ModelForm
from .models import Employee, Company, Department


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "logo", "name", "legal_number",


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



