from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts, name="posts"),
    path('post/detalle/<int:post_id>', views.detalle_post, name="detalle_post"),
]