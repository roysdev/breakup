from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect


from django.views.generic import CreateView, UpdateView

from django.contrib.auth.forms import PasswordChangeForm
from . import forms
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


from django.core.paginator import Paginator

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect("home")

def user_profile(request, username):
    profile_owner = get_object_or_404(User, username=username)
    is_following = False

    if request.user.is_authenticated:
        toggle_user = get_object_or_404(User, username=request.user)

        if toggle_user.profile.following.filter(id=profile_owner.id).exists():
            is_following = True
    # # comment_form = CommentForm()
    # is_liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         # A comment was posted
    #         comment_form = CommentForm(data=request.POST)

    #         if comment_form.is_valid():
    #             new_comment = comment_form.save(commit=False)
    #             new_comment.user = request.user
    #             new_comment.post = post
    #             new_comment.save()
    # model = Post
    # template_name = 'posts/post_list.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'post'  # Default: object_list
    # paginate_by = 10
    # queryset = Post.objects.all() 
    post_list = profile_owner.post.all()
    paginator = Paginator(post_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = { 
                'posts': posts,
                'profile_owner': profile_owner,
                'is_following': is_following
                }
    return render(request, 'accounts/user_detail.html', context )


def follow(request):

    is_following = False

    profile_owner = get_object_or_404(User, username=request.POST.get('profile_user'))
    toggle_user = get_object_or_404(User, username=request.user)

    if toggle_user.profile.following.filter(id=profile_owner.id).exists():
        toggle_user.profile.following.remove(profile_owner)
        is_following = False
    else:
        toggle_user.profile.following.add(profile_owner)
        is_following = True

    return redirect("account:detail", username=profile_owner.username)


def following_list(request, username):
    profile_owner = get_object_or_404(User, username=username)

    following_list = profile_owner.profile.get_following()
    paginator = Paginator(following_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    followings = paginator.get_page(page)
    context = { 
                'followings': followings,
                'profile_owner': profile_owner,
                }
    return render(request, 'accounts/following_list.html', context )


def followers_list(request, username):
    profile_owner = get_object_or_404(User, username=username)

    followers_list = profile_owner.followed_by.all()
    paginator = Paginator(followers_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    followers = paginator.get_page(page)
    context = { 
                'followers': followers,
                'profile_owner': profile_owner,
                }
    return render(request, 'accounts/followers_list.html', context )


def edit_icon(request):
    if request.method == 'POST':
        form = forms.EditIconForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            # messages.sucess(request, f'Profile Picture Updated!')
            return redirect("account:edit")
    else:
        form = forms.EditIconForm(instance=request.user.profile)
        context = {'form': form}
        return render(request, 'accounts/edit_icon.html', context)

def edit_email(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
        
            return redirect("account:edit")
    else:
        form = forms.EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'accounts/edit_email.html', context)

# def edit_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect("account:edit")
#     else:
#         form = PasswordChangeForm(user=request.user)
#         context = {'form': form}
#         return render(request, 'accounts/edit_password.html', context)


def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')