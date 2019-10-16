from django.urls import path, include
from . import views


from django.views.generic.base import RedirectView

from .views import (PostListView, 
                    PostCreateView, PostUpdateView, PostDeleteView)

app_name='posts'
urlpatterns = [
    path('', PostListView.as_view(), name="list"),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.post_detail, name='detail'),

    path('like/', views.like_post, name='like_post'),


]


