from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse


# Create your views here.

def index_view(request):
    return render(request, 'home.html')


def reg_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')

            data = RegistrationData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                mobile=mobile,
                email=email
            )
            data.save()
            return redirect('/#/')
        else:
            return HttpResponse("all fields are mandatory")
    else:
        rform = RegistrationForm()
        return render(request, 'registration.html', {'rform': rform})


def login_view(request):
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username', '')
            pwd = request.POST.get('password', '')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password=pwd)
            if uname1 and pwd1:
                return HttpResponse("you have given corerct username and password")
            else:
                return HttpResponse("you have given wrong details")
    else:
        lform = LoginForm()
        return render(request, 'login_form.html', {'lform': lform})