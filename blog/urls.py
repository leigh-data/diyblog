from django.urls import path

from .views import HomePageView, BloggerListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('bloggers/', BloggerListView.as_view(), name='bloggers')
]
