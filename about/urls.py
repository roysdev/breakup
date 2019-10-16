from django.urls import path, include
from . import views



# from .views import (PostListView)

app_name='site'
urlpatterns = [
    path('about', views.about , name="about"),


]


