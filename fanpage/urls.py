from django.urls import path
from . import views

app_name = "fanpage"

urlpatterns = [
    path("main", views.index, name="main"),
    path("post/add", views.add, name="post_add"),
    path("post/edit/<int:pk>", views.edit, name="post_edit"),
    path("post/delete/<int:pk>", views.delete, name="post_delete"),
]