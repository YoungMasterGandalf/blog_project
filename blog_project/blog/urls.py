from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.blog_list, name='blog_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
