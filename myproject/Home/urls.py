from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index),
    path("my/", views.myHtml),
    path("emp/", views.reg_emp),
    path("stu/", views.stud_reg),
    path("a/", views.about),
    path("f/",views.file_upload),
    path("ss/",views.setsession,name="ss"),
    path("gs/",views.viewsession),
    path("ms/",views.mysession),
    path("ds/",views.delsession),
    path("sc/",views.set_c),
    path("gc/",views.get_c),
    path("m/",views.mail),





    




]