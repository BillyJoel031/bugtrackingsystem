from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    context= {'form':form, 'msg': msg}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg= 'User Created'
            return redirect(login_view)
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method =="POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg= 'invalid credentials'
        else:
            msg= 'error validating form'
    return render(request,'login.html', {'form':form, 'msg':msg})

def home(request):
    return render(request, 'homepage.html')
