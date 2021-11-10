from django.contrib import admin

# Register your models here.
from core.models import Company, Employee, Department

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Company)
