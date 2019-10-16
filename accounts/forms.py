from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 
from .models import UserProfile
from django.core.files.images import get_image_dimensions

from .mixins import EmailRequiredMixin

class UserSignUpForm(EmailRequiredMixin, UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['email'].required = True
# class UserProfileEdit(forms.modelForm):

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            'email',
        )

class EditIconForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = (
            'image',
        )
