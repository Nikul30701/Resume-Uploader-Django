from django.db import IntegrityError
from django.shortcuts import render, redirect
from  .forms import ResumeForms
from .models import Resume
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm,pwd)
        try:
            my_user = User.objects.create_user(username=fnm, email=email, password=pwd)
            my_user.save()
            print("user created successfully")
            return redirect('login')
        except IntegrityError:
            print("Username already exists")
            return render(request, 'signup.html', {'error': 'Username already exists. Please choose another one.'})
    return render(request, "signup.html")


def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            print("logged in!")
            return redirect("home")
        else:
            return redirect('login.html',{'error': 'Invalid username or password. Please try again.'})
    return render(request, "login.html")


class HomeView(View):
    def get(self, request):
        form = ResumeForms()
        candidates = Resume.objects.all()
        return render(request, "home.html", {'candidates': candidates, 'form': form})

    def post(self, request):
        form = ResumeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            candidates = Resume.objects.all()
            return render(request, "home.html", {'candidates': candidates, 'form': form})


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate': candidate})


