from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required



from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from comments.models import Comment


from comments.forms import CommentForm
from .models import SiteUpdate, Blog



                    


def about(request):
    blog = Blog.objects.order_by('-timestamp')[0:1]
    news = SiteUpdate.objects.order_by('-timestamp')[0:1]


    # comment_form = CommentForm()
    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         # A comment was posted
    #         comment_form = CommentForm(data=request.POST)

    #         if comment_form.is_valid():
    #             # Create Comment object but don't save to database yet
    #             new_comment = comment_form.save(commit=False)

    #             # Assign the current post to the comment
    #             new_comment.user = request.user
    #             new_comment.post = post
    #             # Save the comment to the database
    #             new_comment.save()
        
    
    context = { 'blog': blog,
                'news': news }
    return render(request, 'about.html', context )
                                                     
# def like_post(request):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     is_liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         is_liked = False
#     else:
#         post.likes.add(request.user) 
#         is_liked = True
#     return HttpResponseRedirect(post.get_absolute_url())



