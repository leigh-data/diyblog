from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import CommentForm, BlogForm
from .helpers import PERM


class HomePageView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    permission_required = [PERM]
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = BlogForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object()
        return context

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.post = self.get_object()
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        return Comment.objects.all()

    def get_initial(self):
        initial = super().get_initial()
        comment = self.get_object()
        initial['commenter'] = comment.commenter
        initial['post'] = comment.post
        initial['description'] = comment.description

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = self.get_object()
        context["post"] = Post.objects.get(pk=comment.post.pk)
        return context

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.commenter != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    context_object_name = "comment"
    success_url = reverse_lazy("blog:index")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.commenter != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BloggerListView(ListView):
    queryset = get_user_model().objects.filter(user_permissions=PERM)
    context_object_name = "bloggers"
    template_name = 'blog/bloggers.html'


class BloggerDetailView(DetailView):
    queryset = get_user_model().objects.filter(user_permissions=PERM)
    context_object_name = "blogger"
    template_name = 'blog/blogger.html'
