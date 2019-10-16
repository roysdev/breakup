
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from comments.models import Comment


from comments.forms import CommentForm
from .forms import PostModelForm

from django.core.paginator import Paginator


class PostCreateView(FormUserNeededMixin, CreateView):
    form_class = PostModelForm
    template_name = 'posts/create_view.html'

class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'posts/update_view.html'
    # success_url = '/..'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_confirm.html'
    def get_success_url(self):
        return reverse_lazy('account:detail', kwargs={'username': self.object.user.username})
    

class PostListView(ListView):
    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query) |
                    Q(title__icontains=query)
                    )
        return qs
    

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context
    paginate_by = 8
                    


def post_detail(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.user.is_authenticated:
        if request.method == 'POST':
            # A comment was posted
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)

                # Assign the current post to the comment
                new_comment.user = request.user
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
        
    
    context = { 'post': post,
                'is_liked': is_liked,
                'comment_form': comment_form }
    return render(request, 'posts/post_detail.html', context )
                                                     
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user) 
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())



