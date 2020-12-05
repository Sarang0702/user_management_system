from django.shortcuts import render, redirect
from django.contrib import messages
from app1.models import Student, Teacher, Institute


def home(request):
    return render(request,"home.html")


def student(request):
    return render(request, "student.html")


def savestudent(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    mob = request.POST.get("mob")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")

    if pass1 == pass2:
        Student(firstname=fname,lastname=lname,email=email,phone=mob,password=pass1).save()
        messages.success(request,"Registration Successful")
        return redirect("student")

    else:
        return render(request,"regstudent.html",{"msg":"Password Not Match"})

def loginstudent(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        data = Student.objects.get(email=email,password=password)
        return render(request, "loginstudent.html", {"data": data})

    except:
        messages.success(request, "Invalid Account")
        return redirect("home")

def regstudent(request):
    return render(request,"regstudent.html")

def teacher(request):
    return render(request,"teacher.html")


def loginteacher(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        data = Teacher.objects.get(email=email, password=password)
        return render(request, "loginteacher.html", {"data": data})

    except:
        messages.success(request, "Invalid Account")
        return redirect("home")


def regteacher(request):
    return render(request,"regteacher.html")


def saveteacher(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    mob = request.POST.get("mob")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")

    if pass1 == pass2:
        Teacher(firstname=fname, lastname=lname, email=email, phone=mob, password=pass1).save()
        messages.success(request, "Registration Successful")
        return redirect("teacher")

    else:
        return render(request, "regteacher.html", {"msg": "Password Not Match"})


def institute(request):
    return render(request,"institute.html")


def logininstitute(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        data = Institute.objects.get(email=email, password=password)
        return render(request, "logininstitute.html", {"data": data})

    except:
        messages.success(request, "Invalid Account")
        return redirect("home")


def reginstitute(request):
    return render(request,"reginstitute.html")


def saveinstitute(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    mob = request.POST.get("mob")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")

    if pass1 == pass2:
        Institute(firstname=fname, lastname=lname, email=email, phone=mob, password=pass1).save()
        messages.success(request, "Registration Successful")
        return redirect("teacher")

    else:
        return render(request, "reginstitute.html", {"msg": "Password Not Match"})
