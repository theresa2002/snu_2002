"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))cm
"""
from django.contrib import admin
from django.urls import path,include
from Stud import views as st

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("Home.urls")),
    path('emp/', include("emp.urls")),
    path("h/",st.hai), 
    path("reg/",st.stud_add),
    path("view/",st.view_stud),
    path("de/<int:sid>/",st.del_stud),
    path("edit/<int:sid>/",st.edit_stud),
    path("update/<int:sid>/",st.update_stud),
    path('ssu/',st.stud_signup),
    path('sst/',st.teacher_signup),
    path('emp/',st.employee),
    path('si/',st.sign_in),
    path('ah/',st.admin_home,name="admin_home"),
    path('sh/',st.stud_home,name="stud_home11"),
    path('edit_pro/',st.stud_edit_profile,name='edit_pro1'),
    path('logout/',st.logout,name='lg'),









    
]
