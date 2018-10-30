from django.urls import path, include
from .views import BlogView, BlogCreateView, BlogUpdateView, DestroyView

urlpatterns = [
    path('', BlogView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='create-blog'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update-blog'),
    path('delete/<int:pk>/', DestroyView.as_view(), name='delete-blog')
]
