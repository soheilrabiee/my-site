from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request=request, template_name="blog/index.html")


def posts(request):
    return render(request=request, template_name="blog/all-posts.html")


def post_detail(request, slug):
    return render(request=request, template_name="blog/post-detail.html")
