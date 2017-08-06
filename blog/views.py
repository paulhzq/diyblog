from django.shortcuts import render
from .models import Post,Comment,Author
# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    #
    return render(request,'index.html',context={})
