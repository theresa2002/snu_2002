from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from emp.models import Employee
from django.urls import reverse_lazy

# Create your views here.

class Empcreateview(CreateView):
    model=Employee
    template_name="emp_reg.html"
    fields="__all__"
    success_url=reverse_lazy("emp_user_list")


class EmpListView(ListView):
    model=Employee
    template_name="emp_list.html"
    context_object_name="oo"


class EmpDelete(DeleteView):
    model=Employee
    template_name="employee_confirm_delete.html"
    success_url=reverse_lazy("emp_user_list")
