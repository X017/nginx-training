from django.urls import path
from .views import TimelineView, DaisyUILoginView, DaisyUIRegisterView, TweetCreateView, TweetUpdateView, TweetDeleteView, TweetListView

app_name = 'tweets'
urlpatterns = [
    path('login/', DaisyUILoginView.as_view(), name='login'),
    path('register/', DaisyUIRegisterView.as_view(), name='register'),
    path('', TweetListView.as_view(), name='list'),
    path('new/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
]

