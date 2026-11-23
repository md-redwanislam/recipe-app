from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    bio = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=20)
    bio = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)