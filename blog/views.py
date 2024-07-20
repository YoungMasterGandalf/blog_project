from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Blog, Tag
from .forms import SearchForm


def homepage(request):
    latest_blogs = Blog.objects.all().order_by("-created_at")[:3]
    tags = Tag.objects.all()

    return render(
        request, "blog/homepage.html", {"latest_blogs": latest_blogs, "tags": tags}
    )


def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "blog/blog_list.html", context)


def blog_tag(request, tag):
    blogs = Blog.objects.filter(tags__name__icontains=tag).order_by("-created_at")
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "tag": tag}

    return render(request, "blog/blog_tag.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {"blog": blog}

    return render(request, "blog/blog_detail.html", context)


def search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Blog.objects.filter(
                Q(title__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()

    context = {"form": form, "query": query, "results": results}

    return render(request, "blog/search.html", context)
