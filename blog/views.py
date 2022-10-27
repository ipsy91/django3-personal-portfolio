from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def all_blogs(request):
    length = len(Blog.objects.all())
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html', {
        'length': length,
        'blogs': blogs,

    })


def detail(request, id_blog):
    blog = get_object_or_404(Blog, pk=id_blog)
    return render(request, 'blog/One_blog.html', {
        'blog': blog,
    })
