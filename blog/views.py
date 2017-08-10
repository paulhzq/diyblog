from django.shortcuts import render
from .models import Post,Comment,Author
from django.views import generic

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    #
    return render(request,'index.html',context={})

class BlogListView(generic.ListView):
    model = Post;

class BlogDetailView(generic.DetailView):
    model = Post;
