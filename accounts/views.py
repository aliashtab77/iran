from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from accounts.forms import ProfileForm



# Create your views here.

def testre(request):
    z = ProfileForm()
    return render(request, 'test.html', {'zz':z})




def loginview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("ورود انجام شد")
        else:
            context = {
                'username': username,
                "erorremas": "کاربری با این مشخصات یافت نشد"
            }
            return render(request, 'baselogin.html', context=context)

    return render(request, "baselogin.html")


def logoutview(request):
    logout(request)
    return HttpResponse("خروج انجام شد")


def register(request):
    return render(request, "base-register.html")
