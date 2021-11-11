from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from core.models import Company, Department, Employee
from .forms import CompanyForm, DepartmentForm, EmployeeForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.shortcuts import render
import csv


def list_company(request):
    companies = Company.objects.all()
    form = CompanyForm
    data = {'companies': companies, 'form': form}
    return render(request, 'core/list_company.html', data)


def create_company(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_company')

# def create_company(request):
#     form = CompanyForm(request.POST or None)
#     if form.is_valid():
#         return HttpResponseRedirect('/thanks/')
#     else:
#         messages.error(request, "Error")
#     return render(request, 'core/list_company.html', {'form': CompanyForm()})

def update_company(request, id):
    data = {}
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)
    data['company'] = company
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_company')
    else:
        return render(request, 'core/update_company.html',  data)


def delete_company(request, id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        company.delete()
        return redirect('core_list_company')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': company})


#===================================================================================


def list_department(request):
    departments = Department.objects.all()
    form = DepartmentForm
    data = {'departments': departments, 'form': form}
    return render(request, 'core/list_department.html', data)


def create_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_department')


def update_department(request, id):
    data = {}
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, instance=department)
    data['department'] = department
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_department')
    else:
        return render(request, 'core/update_department.html',  data)


def delete_department(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('core_list_department')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': department})


#===================================================================================


def list_employee(request):
    employees = Employee.objects.all()
    form = DepartmentForm
    data = {'employees': employees, 'form': form}
    return render(request, 'core/list_employees.html', data)


def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_employee')


def update_employee(request, id):
    data = {}
    employee = Employee.objects.get(id=id)
    form = DepartmentForm(request.POST or None, instance=employee)
    data['employee'] = employee
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_employee')
    else:
        return render(request, 'core/update_employee.html',  data)


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('core_list_employee')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': employee})


#===================================================================================


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Employee_pdf(View):
    def get(self, request):
        employees = Employee.objects.all()
        params = {
            'employees': employees,
            'request': request,
        }
        return Render.render('core/employee-pdf.html', params, 'employee_pdf')

class Employee_csv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employee.csv"'

        employees = Employee.objects.all()

        writer = csv.writer(response)
        writer.writerow([
            'Id',
            'Name',
            'User',
            'Gender',
            'Department',
            'Phone',
            'Role',
            'Age',
            'Joining date',
            'Salary',
            'Create at',
            'Updated at',
            'create_user',
            'Updated_user',
        ])

        for employee in employees:
            writer.writerow(
                [employee.id,
                 employee.name,
                 employee.user,
                 employee.gender,
                 employee.department,
                 employee.phone,
                 employee.role,
                 employee.age,
                 employee.joining_date,
                 employee.salary,
                 employee.created_at,
                 employee.updated_at,
                 employee.create_user,
                 employee.update_user,

                 ])

        return response



# class CreateCompany(CreateView):
#     model = Company
#     fields = [
#             'logo',
#             'name',
#             'legal_number',
#         ]
#
#     success_url = '/core/company-list'
#
#
# class CompanyList(ListView):
#     model = Company
#
# class CompanyEdit(View):
#     def get(self, request, company):
#         data = {}
#         company = Company.objects.get(id=company)
#         data['form'] = CompanyForm()
#         data['logo'] = company.logo
#         data['name'] = company.name
#         data['legal_number'] = company.legal_number
#         return render(request, '/core/company-form.html', data)
