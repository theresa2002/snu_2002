from django.http import HttpResponse
from django.shortcuts import render
from Student.models import User,Student_User



# Create your views here.
def studentreg(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST['username']
        phn=request.POST['phone']
        pw=request.POST['password']

        user_details=User.objects.create_user(first_name=fname,last_name=lname,
        email=email,is_active=0,username=user,phone=phn,password=pw,usertype='Student')
        user_details.save()

        dpt=request.POST['department']
        pm=request.POST['plus two mark']

        details=Student_User.objects.create(department=dpt,plus_mark=pm,user_id=user_details)
        details.save()

        return HttpResponse("<script>window.alert('Successfully Added!!')</script>")
    else:
        return render(request,"student_reg.html")
    


def student_signup(request):
 w
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST['uname']
        phn=request.POST['ph']
        pw=request.POST['pass']

        user_details=User.objects.create_user(first_name=fname,last_name=lname,
        email=email,is_active=0,username=user,phone=phn,password=pw,usertype='Student')
        user_details.save()

        dpt=request.POST['dpt']
        pm=request.POST['pm']

        details=Student_User.objects.create(department=dpt,plus_mark=pm,user_id=user_details)
        details.save()

        return HttpResponse("<script>window.alert('Successfully Updated!!')</script>")
    else:
        return render(request,'student_signup.html')