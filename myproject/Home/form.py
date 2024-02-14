from django import forms
from Home.models import Employee,FileUpload

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        # fields=["first_name","last_name","dob"]
        # exclude=["first_name"]

class StudForm(forms.Form):
    firstname=forms.CharField(label="Enter ur name:",max_length=10)
    email=forms.CharField(label="Enter ur email",max_length=20)

class UploadFile(forms.ModelForm):
    class Meta:
         model=FileUpload
         fields="__all__"       