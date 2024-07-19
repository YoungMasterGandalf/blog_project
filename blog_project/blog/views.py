from django.shortcuts import render
from .models import Blog, Tag


def homepage(request):
    featured_blogs = Blog.objects.all().order_by("-created_at")[:3]
    tags = Tag.objects.all()

    return render(
        request, "blog/homepage.html", {"featured_blogs": featured_blogs, "tags": tags}
    )

