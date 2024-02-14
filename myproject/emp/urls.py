from django.contrib import admin
from django.urls import path,include
from emp.views import *


urlpatterns=[
    path('create/',Empcreateview.as_view(),name='emp_user_create'),
    path('view/',EmpListView.as_view(),name='emp_user_list'),
    path('<int:pk>/del/',EmpDelete.as_view(),name='emp_user_del'),


]
