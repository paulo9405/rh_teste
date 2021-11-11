from django.urls import path
from .views import (
    create_company,
    list_company,
    update_company,
    delete_company,
    create_department,
    list_department,
    update_department,
    delete_department,
    create_employee,
    list_employee,
    update_employee,
    delete_employee,
    Employee_pdf,
    Employee_csv
)


urlpatterns = [

    path('', list_company, name='core_company'),
    path('company/', list_company, name='core_company'),
    path('create-company/', create_company, name='core_create_company'),
    path('update-company/(?P<id>[0-9]+)/$', update_company, name='core_update_company'),
    path('delete-company/(?P<id>[0-9]+)/$', delete_company, name='core_delete_company'),

    path('company/department/', list_department, name='core_department'),
    path('create-department/', create_department, name='core_create_department'),
    path('update-department/(?P<id>[0-9]+)/$', update_department, name='core_update_department'),
    path('delete-department/(?P<id>[0-9]+)/$', delete_department, name='core_delete_department'),

    path('company/employee/', list_employee, name='core_employee'),
    path('create-employee/', create_employee, name='core_create_employee'),
    path('update-employee/(?P<id>[0-9]+)/$', update_employee, name='core_update_employee'),
    path('delete-employee/(?P<id>[0-9]+)/$', delete_employee, name='core_delete_employee'),
    path('employee-pdf/', Employee_pdf.as_view(), name='core_employee_pdf'),
    path('employee-csv/', Employee_csv.as_view(), name='core_employee_csv'),

    # path('company-list', CompanyList.as_view(), name='company_list'),
    # path('company-edit/<int:company>/', CompanyEdit.as_view(), name="company_edit"),

   # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
   # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
   # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
   # path('process-create', ProcessCreate.as_view(), name='process-create'),
   # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
   # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
   # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),




]