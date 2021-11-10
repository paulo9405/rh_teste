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
        fields = '__all__'

# class CompanyForm(forms.Form):
#     company_id = forms.CharField(label='ID do Produto', max_length=100)
#     logo = forms.IntegerField(label='logo')
#     name = forms.CharField(label='Name', max_length=100)
#     legal_number = forms.CharField(label='Legal Number', max_length=20)


