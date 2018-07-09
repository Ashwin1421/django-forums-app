from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from forumsApp.models import Article, Comment


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ArticleCreationForm(forms.Form):
    title = forms.CharField(max_length=150, required=True, help_text="Required. Put an interesting title here!")
    description = forms.CharField(max_length=255, required=False, help_text="Optional. A brief description of what the article is about.")
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False,help_text="Upload a nice picture along with this article.")

    class Meta:
        model = Article
        fields = ('title','description','content','image', 'author')
    
class ProfileViewForm(UserChangeForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','password',)
    

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('text','author',)