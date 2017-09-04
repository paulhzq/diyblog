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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = Comment
    fields = ['content',]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
