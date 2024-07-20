from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
    path('search/', views.search, name='search'),
]
