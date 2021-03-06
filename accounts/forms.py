from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from .idgenerator import id
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)
from django.core.validators import MaxValueValidator, MinValueValidator
User =  get_user_model()
class UserLoginForm(forms.Form):
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        password =self.cleaned_data['password']
        if email and password:
            user = authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError("Incorrect userName or password")
            
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm, self).clean(*args,**kwargs)


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        exclude = ['CSU_ID']
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        exclude = ['CSU_ID']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password  ', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    class Meta:
        model=User
        exclude = ['CSU_ID','password','last_login','active','staff','admin']
