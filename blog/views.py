from django.shortcuts import render
from .models import Post,Comment,Author
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    #
    return render(request,'index.html',context={})

class BlogListView(generic.ListView):
    model = Post

class BlogDetailView(generic.DetailView):
    model = Post

class BloggerListView(generic.ListView):
    model = Author

class BloggerDetailView(generic.ListView):
    # model = Author
    template_name ='blog/author_detail.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        author = Author.objects.filter(id = id)
        return Post.objects.filter(author = author)
    def get_context_data(self, **kwargs):
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        context['author'] = get_object_or_404(Author,pk = self.kwargs['pk'])
        return context
