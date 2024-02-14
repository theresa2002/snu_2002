from django.urls import path
from Student import views as stu

urlpatterns=[
    path("sr/",stu.studentreg),
]