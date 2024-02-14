from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from Home.form import EmpForm,StudForm,UploadFile
from Home.models import FileUpload
from Home.functions.function import upload_file
from myproject import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    # return HttpResponse("hello world")
    return HttpResponse("<h1>hello world</h1>") 

def myHtml(request):
    # temp=loader.get_template("day1.html")
    # name=input("enter your name :")
    # details={"fname":name}
    # return HttpResponse(temp.render(details))
    temp=loader.get_template("day1.html")
    return HttpResponse(temp.render())



def reg_emp(request):
    if request.method=="POST":
        frm=EmpForm(request.POST)
        # print("...............")
        # print(frm)
        # return HttpResponse("helooooooo")
        if frm.is_valid():
            try: 
                return redirect("/")
            except:
                return HttpResponse("error")
                # print("===")
    else:
        # print("/////////////")
        emp=EmpForm()
        return render(request,"emp_reg.html",{"form":emp})



def stud_reg(request):
    s=StudForm()
    return render(request,"stu_reg.html",{"frm":s})

def about(request):
     return render(request,"aboutus.html")


def file_upload(request):
    if request.method=='POST':
        fi=UploadFile(request.POST,request.FILES)
        if fi.is_valid():
            upload_file(request.FILES["file"])
            return HttpResponse("success")
        else:
            return HttpResponse("Error")
    else:
        
        f=UploadFile()
        return render(request,"FileUpload.html",{"form":f})
    
def setsession(request):
    request.session["name"]="ishoo"
    request.session["email"]="ishoo@gmail.com"
    return HttpResponse("session set")

def viewsession(request):
    if "name" in request.session:
        sname=request.session["name"]
        semail=request.session["email"]
        return HttpResponse(sname+"  "+semail)
    else:
        return HttpResponse("please login first")

def mysession(request):
    return render(request,"mypage.html")

def delsession(request):
    if "name" in request.session:
        del request.session["name"]
        del request.session['email']
        return HttpResponse("successfully logout")
    else:
        return HttpResponse("please login first")
    

def set_c(request):
    res=HttpResponse("cookies set")
    res.set_cookie("name","ishoo")
    return res

def get_c(request):
    ename=request.COOKIES["name"]
    return HttpResponse("my name is "+ ename)


def mail(request):
    subject="welcome"
    msg="haai django"
    to="snehatheresa10@gmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        m="success"
    else:
        m="failed"
    return HttpResponse(m)








