from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request=request, template_name="blog/index.html")


def posts(request):
    pass


def post_detail(request):
    pass
