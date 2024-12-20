from django.contrib.auth.decorators import login_required
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
        pwd = request.POST.get('pwd')

        try:
            my_user = User.objects.create_user(username=fnm, password=pwd)
            my_user.save()
            return redirect('/login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Username already exists. Please choose another one.'})
    return render(request, "signup.html")


def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect("/home")
        else:
            return redirect('/login')
    return render(request, "login.html")


class HomeView(View):
    @login_required(login_url='/login')
    def get(self, request):
        form = ResumeForms
        candidates = Resume.objects.all()
        return render(request,"Home.html",
                      {'candidates':candidates, 'form':form})

    def post(self, request):
        form = ResumeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


class CandidateView(View):
    @login_required(login_url='/login')
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'candidate.html', {'candidate':candidate})