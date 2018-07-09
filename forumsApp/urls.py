from django.urls import path
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "forumsApp"
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path("", views.index, name="index"),
    path("articles/", views.index, name="articles"),
    path("article/<int:pk>/", views.article_detail_view, name="article-detail"),
    path("loginView/",views.loginView, name="loginView"),
    path("signup/", views.signup, name="signup"),
    path("logoutView/", views.logoutView, name="logout"),
    path("newArticle/", views.newArticle, name="new_article"),
    path("accounts/profile/", views.index, name="profile"),
    path("profile/", views.profile, name="profileView"),
    path("changePassword/", views.change_password, name="updatePassword"),
    path("^article/(?P<pk>\d+)/add_comment/$", views.add_comment, name="article_comment"),
]
