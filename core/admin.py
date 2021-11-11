from django.contrib import admin
from core.models import Company, Employee, Department


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Company)
