from django.urls import path
from .views import DaisyUILoginView, DaisyUIRegisterView, CreateBlogPostView, ViewBlogPostsViews, BlogPostUpdateView, BlogPostDeleteView, CreateCategoryView



app_name = 'blog'
urlpatterns = [
    path('login/', DaisyUILoginView.as_view(), name='login'),
    path('register/', DaisyUIRegisterView.as_view(), name='register'),
    path('create-blog/', CreateBlogPostView.as_view(), name='create_blog'),
    path('', ViewBlogPostsViews.as_view(), name='post_list'),
    path('posts/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete_post'),
    path('category/create/', CreateCategoryView.as_view(), name='create_category'),
]
