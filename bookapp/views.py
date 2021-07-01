from django.shortcuts import render,redirect
from .forms import BookCreateForm
from .models import Book
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .decorators import login_required,admin_only

# def login_required(func):
#     def wrapper(request,*args,**kwargs):
#         if not request.user.is_authenticated:
#             return redirect("login")
#         return func(request,*args,**kwargs)
#     return wrapper
#
# def admin_only(func):
#     def wrapper(request,*args,**kwargs):
#         if not request.user.is_superuser:
#             return redirect("login")
#         return func(request,*args,**kwargs)
#
#     return wrapper


@admin_only
def create_book(request):
    form=BookCreateForm()
    context={}
    context["forms"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            # b_name=form.cleaned_data.get("book_name")
            # author=form.cleaned_data.get("author")
            # page=form.cleaned_data.get("pages")
            # price=form.cleaned_data.get("price")
            # book=Book(book_name=b_name,author=author,pages=page,price=price)
            # print("saved")
            #
            # book.save()
            form.save()
            return redirect("list")


    return render(request,"bookapp/createbook.html",context)

@login_required
def list_all_books(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"bookapp/listofbooks.html",context)
@login_required
def book_detail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"bookapp/bookdetail.html",context)
@admin_only
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")
@admin_only
def update_book(request,id):
    book=Book.objects.get(id=id)
    form=BookCreateForm(instance=book)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request, "bookapp/editbook.html", context)


def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"bookapp/login",context)
        else:
            form=UserRegistrationForm(request.POST)

            context["form"] = form
            return redirect("login")
    return render(request,"bookapp/registration.html",context)


def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            user=authenticate(request,username=username,password=password)
            if user:
                print("test")
                login(request,user)
                return redirect("list")
    return render(request,"bookapp/login.html",context)

def signout(request):
    logout(request)
    return redirect("login")
@login_required
def user_home(request):
    return render(request,"bookapp/index.html")
