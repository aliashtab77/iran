from django import forms
from accounts.models import ProfileModel
from phonenumber_field.formfields import PhoneNumberField

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={}))
    phone = PhoneNumberField(region="IR", widget=forms.TextInput(attrs={}))
    # email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={}))
    # rule = forms.BooleanField(widget=forms.)

    class Meta:
        model = ProfileModel
        fields = ['phone', 'rule']
