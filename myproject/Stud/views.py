from django.shortcuts import render,redirect
from django.http import HttpResponse
from Stud.form import StudentForm
from Stud.models import Student,User,Employee,stud_user
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def hai(request):
    return HttpResponse("<h1>hello student</h>")

def stud_add(request):
    if request.method=="POST":
        stufrm=StudentForm(request.POST)
        if stufrm.is_valid():
            stufrm.save()
            # return redirect("/view/")
            # return HttpResponse("<h1>success</h1>")
            return HttpResponse("<script>window.alert('Successfully Added!!');window.location.href='/view'</script>")
        else:
            return HttpResponse("<h1>error</h1>")
    else:        
        stu=StudentForm()
        return render(request,"stud_reg.html",{"form":stu})
    

def view_stud(request):
        details=Student.objects.all()
        return render(request,"view_stud.html",{"data":details})


def del_stud(request,sid):
    print("..........",sid)
    stu=Student.objects.get(id=sid)
    stu.delete()
    
    #  return HttpResponse("<h1>deleted</h1>")
    return HttpResponse("<script>window.alert('Successfully deleted!!');window.location.href='/view'</script>")

def edit_stud(request,sid):
     
    stu=Student.objects.get(id=sid)
    #  print("-------------",sid)
    return render(request,"edit_stud.html",{"data":stu})

def update_stud(request,sid):
    st=Student.objects.get(id=sid)
    form=StudentForm(request.POST,instance=st)
    if form.is_valid():
        form.save()
        return HttpResponse("<script>window.alert('Successfully updated!!');window.location.href='/view'</script>")
    else:
        return HttpResponse("<script>window.alert('error occured!!');window.location.href='/view'</script>")



    




def stud_signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST['uname']
        phn=request.POST['ph']
        pw=request.POST['pass']

        print('...................',user,email)
        

        user_details=User.objects.create_user(first_name=fname,last_name=lname,
        email=email,username=user,phone=phn,password=pw,usertype='Student')

        user_details.save()
        pm=request.POST["pm"]
        dpt=request.POST["dpt"]
        details=stud_user.objects.create(department=dpt,plus_mark=pm,user_id=user_details)

        return HttpResponse("<script>window.alert('Successfully Updated!!')</script>")
    else:
        return render(request,'stud_signup.html')
    
    

def teacher_signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST['uname']
        phn=request.POST['ph']
        pw=request.POST['pass']

        User.objects.create_user(first_name=fname,last_name=lname,
        email=email,username=user,phone=phn,password=pw,usertype='teacher')

        return HttpResponse("<script>window.alert('Successfully Updated!!')</script>")
    else:
        return render(request,'teacher_signup.html')
    
#  ---------------------------------------------------------------------------------------------   
    

def employee(request):
    if request.method=='POST':
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            age=request.POST['age']
            phone=request.POST['phone']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            a=Employee.objects.create(first_name=firstname,last_name=lastname,
            age=age,phone=phone,
            email=email,username=username,
            password=password
            )
            a.save()
            return HttpResponse('Success')

    else:
        return render(request,'employee.html')


def emp_view(request):
    details=Employee.objects.all()
    return render(request,"emp_view.html",{"data":details})

@login_required
def sign_in(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pw=request.POST['pw']

        user=authenticate(username=uname,password=pw)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("admin_home")
            elif user.usertype=="Student":
                request.session["stud_id"]=user.id
                return redirect('stud_home11')
            
            return HttpResponse("<script>window.alert('Successful login!!')</script>")
        else:
            return HttpResponse("<script>window.alert('Incorrect Username or password!!')</script>")
        
    else:
        return render(request,'signin.html')
    

@login_required
def admin_home(request):
    return render(request,'admin_home.html')  

@login_required
def stud_home(request):
    return render(request,'stud_home.html')    
 
   
@login_required
def stud_edit_profile(request):
    if request.method=="GET":
        sid=request.session["stud_id"]
        data=User.objects.get(id=sid)
        data1=stud_user.objects.select_related("user_id").get(id=sid)
        data2=stud_user.objects.select_related("user_id").all()
        return render(request,'edit_profile.html',{"details":data,"details1":data1,"details2":data2})    

    else:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        user=request.POST['uname']
        phn=request.POST['ph']

        user_details=User.objects.create_user(first_name=fname,last_name=lname,
        email=email,username=user,phone=phn,usertype='Student')

        user_details.save()

        pm=request.POST["pm"]
        dpt=request.POST["dpt"]
        user_details.save()

        # details=stud_user.objects.create(department=dpt,plus_mark=pm,user_id=user_details)

@login_required
def logout(request):
    logout(request)
    return redirect(sign_in)
 











