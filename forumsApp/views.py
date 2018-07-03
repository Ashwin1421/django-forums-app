from django.shortcuts import render, get_object_or_404, redirect
from forumsApp.models import Article
from forumsApp.forms import SignUpForm, ArticleCreationForm, LoginForm, ProfileViewForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    template_name = "articles/index.html"
    article_list = Article.objects.filter(published=True)

    return render(request, template_name, { 'article_list': article_list})


def loginView(request):
    template_name = "registration/login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, template_name, { "error" : "Incorrect username/password or both."})

    else:
        form = LoginForm()
    return render(request, template_name, { 'form' : form })

@login_required
def logoutView(request):
    template_name = "registration/logout.html"
    logout(request)
    
    return render(request, template_name)


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

@login_required
def newArticle(request):
    template_name = "articles/new_article.html"
    print(request.user)
    if request.method == "POST":
        form = ArticleCreationForm(request.POST)
        if form.is_valid():
            new_article = Article()
            new_article.title = form.cleaned_data.get("title")
            new_article.description = form.cleaned_data.get("description")
            new_article.content = form.cleaned_data.get("content")
            if request.user.is_authenticated:
                new_article.author = request.user.last_name+", "+request.user.first_name
                
            new_article.save()

            return redirect("/")
    else:
        form = ArticleCreationForm()
    
    return render(request, template_name, { 'form' : form })

@login_required
def profile(request):
    template_name = "profile/profile_view.html"
    if request.method == "POST":
        form = ProfileViewForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            
            return redirect("/")
    else:
        form = ProfileViewForm(instance=request.user)
    
    return render(request, template_name, { 'form' : form })
    

@login_required
def change_password(request):
    template_name = "registration/updatePassword.html"
    
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was changed successfully!")
            login(request, user)
            return redirect("/")
    else:
        form = SetPasswordForm(request.user)
    
    return render(request, template_name, { 'form' : form })
    