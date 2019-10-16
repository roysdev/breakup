from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .mixins import EmailRequiredMixin

# Register your models here.
from .models import UserProfile


class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass

class EmailRequiredUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {
        'fields': ('username', 'email', 'password1', 'password2'), 
        'classes': ('wide',)
    }),)

admin.site.unregister(User)
admin.site.register(User, EmailRequiredUserAdmin)


admin.site.register(UserProfile)