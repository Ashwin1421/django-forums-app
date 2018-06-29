from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forumsApp.models import Article


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

    class Meta:
        model = Article
        fields = ('title','description','content','author')