from django.shortcuts import render, get_object_or_404, redirect
from forumsApp.models import Article
from forumsApp.forms import SignUpForm, ArticleCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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