from django.contrib import admin
from django.urls import path
from .views import (
    post_create,
    post_detail,
    post_home,
    post_list,
    post_update,
    post_delete,
)

urlpatterns = [
    # path('', views.post_home)
    path('create', post_create),
    path('<int:id>/', post_detail, name='detail'),
    path('', post_list, name='list'),
    path('<int:id>/edit', post_update, name="update"),
    path('<int:id>/delete', post_delete),

    # path('', views.post_home, name='home'),
]