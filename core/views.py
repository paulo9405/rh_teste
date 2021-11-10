from django.shortcuts import render, redirect
from core.models import Company, Department, Employee
from .forms import CompanyForm, DepartmentForm, EmployeeForm


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
