from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.shortcuts import HttpResponseRedirect
# Create your views here.

def retrive_data(request):
    employee = Employee.objects.all()

    return render(request , 'testapp/index.html' , {'employee':employee})


def create_data(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect("/")

    return render(request , 'testapp/create.html' , {'form':form})


def delete_data(request ,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('/')


def update_data(request , id):
    employee = Employee.objects.get(id = id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST , instance = employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request , 'testapp/update.html' ,{'employee':employee})
