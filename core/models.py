import uuid
from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string
from django.core.mail import send_mail



# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    logo = models.ImageField(upload_to='logo', null=True)

    name = models.CharField(max_length=100, null=True)
    legal_number = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True, null=True)
    admin = models.UUIDField(editable=False, null=True)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        data = {'company': self.company,
                'name': self.name,
                'status': self.status,
                }

        plain_text = render_to_string('core/emails/new_department.txt', data)
        html_email = render_to_string('core/emails/new_department.html', data)
        send_mail(
            'New department created',
            plain_text,
            'paulo.ricardo1137.pr@gmail.com',
            ['paulo.ricardo1137.pr@gmail.com'],
            html_message=html_email,
            fail_silently=False,
        )

        return super(Department, self).save(*args, **kwargs)


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    gender = models.CharField(max_length=1, choices=GENDER)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    role = models.CharField(max_length=50, default='Sem Atribuição')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)
