from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TweetMessage
from .forms import TweetForm
from django.db.models import Count

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
    success_url = '/list'
    
    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful! Please log in.')
        return response

    def form_invalid(self,form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)




class TweetCreateView(LoginRequiredMixin, CreateView):
    model = TweetMessage
    form_class = TweetForm
    template_name = 'tweets/create.html'
    success_url = reverse_lazy('tweets:list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = TweetMessage
    form_class = TweetForm
    template_name = 'tweets/edit_tweets.html'
    success_url = reverse_lazy('tweets:update',kwargs={'path': '/twit/'})  # Redirect to tweet list after edit
    
   #def get_queryset(self):
   #    """Ensure users can only edit their own tweets."""
   #    return super().get_queryset().filter(author=self.request.user)

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = TweetMessage
    success_url = reverse_lazy('tweets:list')
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class TweetListView(LoginRequiredMixin, ListView):
    model = TweetMessage
    template_name = 'tweets/list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return TweetMessage.objects.all().order_by('-created_at')


class TimelineView(LoginRequiredMixin, ListView):
    model = TweetMessage
    template_name = 'tweets/timeline.html'
    context_object_name = 'tweets'
    paginate_by = 10
    
    def get_queryset(self):
        return TweetMessage.objects.filter().all()
