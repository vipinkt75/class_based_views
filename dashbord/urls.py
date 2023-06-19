from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("navbar/", views.navbar, name="navbar"),
    path("index/", views.index, name="index"),
    path("buttons/", views.buttons, name="buttons"),
    path("login/", views.login, name="login"),
    path("index_page/", views.Index.as_view(), name="main_index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("books/<str:pk>/", views.BookDetailView.as_view(), name="book_detail"),
]
