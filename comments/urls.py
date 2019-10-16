from django.urls import path, include
from . import views

from django.views.generic.base import RedirectView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name='posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]
