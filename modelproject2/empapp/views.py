from django.shortcuts import render
from empapp.models import Employee
from django.http import HttpResponse

# Create your views here.

def boots_view(request):
    return render(request,"empapp/boots.html")

def emp_view(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    context=my_dict
    return render(request,"empapp/emp.html",context)


