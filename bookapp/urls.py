"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import create_book,list_all_books,book_detail,delete_book,update_book,registration,login_user,user_home


urlpatterns = [
    path("createbook",create_book,name="create"),
    path("list",list_all_books,name="list"),
    path("detail/<int:id>",book_detail,name="detail"),
    path("delete/<int:id>",delete_book,name="delete"),
    path("edit/<int:id>",update_book,name="edit"),
    path("registration",registration,name="registration"),
    path("login",login_user,name="login"),
    path("home",user_home,name="home")

]
