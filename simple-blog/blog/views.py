from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BlogPost

class DaisyUILoginView(LoginView):
    template_name = 'login.html'
    def form_valid(self, form):
        messages.success(self.request, 'Login successful! Welcome back.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login failed. Please check your credentials.')
        return super().form_invalid(form)


class DaisyUIRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'blog/login'
    
    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response

    def form_invalid(self,form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class CreateBlogPostView(LoginRequiredMixin,CreateView):
    model = BlogPost
    fields = ['title','text','category']
    template_name = 'create_blog.html'
    success_url = '/blog'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author here
        return super().form_valid(form)
class ViewBlogPostsViews(ListView):
    model = BlogPost
    template_name = 'all_blogs.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['text']
    template_name = 'edit_post.html'
    
    def get_queryset(self):
        # Only allow authors to edit their own posts
        return super().get_queryset().filter(author=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('post_list')  # Redirect to post list after edit



class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:post_list')
    
    # Skip template rendering entirely
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    # Only allow authors to delete
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
