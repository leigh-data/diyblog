from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Post, Comment
from .forms import CommentForm

PERM = Permission.objects.get(codename='blogger')


class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self):
        pass


class BloggerListView(ListView):
    queryset = get_user_model().objects.filter(user_permissions=PERM)
    context_object_name = "bloggers"
    template_name = 'blog/bloggers.html'
