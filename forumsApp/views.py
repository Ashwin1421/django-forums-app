from django.shortcuts import render, get_object_or_404, redirect
from forumsApp.models import Article, SignUpForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def index(request):
    template_name = "articles/index.html"
    article_list = Article.objects.filter(published=True)

    return render(request, template_name, { 'article_list': article_list})


def loginView(request):
    template_name = "registration/login.html"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, template_name, { "error" : "Incorrect username/password or both."})

    return render(request, template_name, {})

def logoutView(request):
    
    logout(request)
    
    return redirect('/')


def signup(request):
    template_name = "registration/register.html"

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        
    return render(request, template_name, { 'form':form })