# forms.py
from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.fields['old_password'].label = 'Old Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'
