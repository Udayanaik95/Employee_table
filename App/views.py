from django.shortcuts import render
from App.models import *
# Create your views here.

def display_dept(request):

    DOA=Department.objects.all()

    d={'Depts':DOA}

    return render(request,'display_dept.html',context=d)

def display_emp(request):

    DOE=Employee.objects.all()

    d={'Emps':DOE}

    return render(request,'display_emp.html',context=d)
