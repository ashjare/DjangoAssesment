from django.shortcuts import render, HttpResponseRedirect
from .models import emp_details
from .forms import EmpDetailsForm
# Create your views here.

# This Function add and show new records
def create_show(request):
    if request.method == "POST":
        fm = EmpDetailsForm(request.POST)
        if fm.is_valid():
            print("Form is valid")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = emp_details(name=name,email=email,password=password)
            reg.save()
            fm = EmpDetailsForm()
    else:
        fm = EmpDetailsForm()
    data = emp_details.objects.all()
    return render(request,'create_delete.html',{"form":fm, "data":data})

# This Function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = emp_details.objects.get(pk=id)
        fm = EmpDetailsForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = emp_details.objects.get(pk=id)
        fm = EmpDetailsForm(instance=pi)
    return render(request, 'update.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = emp_details.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')