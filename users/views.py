from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def create_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if request.method == "POST":
        account = User.objects.create_user(username=username,password=password)
        account.save()
        return redirect("dashboard")
    return render(request,"signin.html")


def login_form(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        error_message = "Invalid username or password."
        return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


def dashboard(request):
    students = Student.objects.all()
    return render(request, "dashboard.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        return HttpResponse("Form is not valid")

    form = StudentForm()
    return render(request, "add_student.html", {"form": form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = StudentForm(instance=student)
        return render(request, "edit_student.html", {"form": form})

    form = StudentForm(instance=student)
    return render(request, "edit_student.html", {"form": form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect("dashboard")
    return render(request, "dashboard.html")

def search_student(request):
    query = request.GET.get("query")
    if query:
        students = Student.objects.filter(student_name=query)
    else:
        students = Student.objects.all()
    return render(request, "dashboard.html", {"students": students})
