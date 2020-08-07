from django.urls import path

from .views import (HomePageView, BloggerListView, BloggerDetailView, BlogDetailView,
                    CommentCreateView, CommentUpdateView, CommentDeleteView, BlogCreateView, BlogUpdateView)

app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/comment/update',
         CommentUpdateView.as_view(), name='comment_update'),
    path('<int:pk>/comment/delete',
         CommentDeleteView.as_view(), name='comment_delete'),
    path('bloggers/', BloggerListView.as_view(), name='bloggers'),
    path('bloggers/<int:pk>', BloggerDetailView.as_view(), name='blogger')
]
