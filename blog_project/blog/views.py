from django.shortcuts import render
from .models import Blog, Tag
from django.core.paginator import Paginator


def homepage(request):
    featured_blogs = Blog.objects.all().order_by("-created_at")[:3]
    tags = Tag.objects.all()

    return render(
        request, "blog/homepage.html", {"featured_blogs": featured_blogs, "tags": tags}
    )


def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "blog/blog_list.html", context)


def tag_list(request):
    tags = Tag.objects.all()
    context = {"tags": tags}

    return render(request, "blog/tag_list.html", context)

