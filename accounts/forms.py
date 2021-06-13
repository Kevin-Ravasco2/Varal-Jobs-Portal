from django.contrib.auth import get_user_model
from django.forms import TextInput, EmailInput, PasswordInput
from django import forms

from accounts.models import MTO

User = get_user_model()


class SignUpForm(forms.Form):
    full_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'first middle last'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    paypal_id = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter paypal ID'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Passwords did not match', code='invalid password')
        if User.objects.using('vendor_os_db').filter(username=email).exists():
            raise forms.ValidationError('A user with that username already exists', code='invalid username')
        return

    def save(self):
        cleaned_data = super().clean()
        full_name = cleaned_data['full_name']
        email = cleaned_data['email']
        paypal_id = cleaned_data['paypal_id']
        password = cleaned_data['password']

        mto = MTO(full_name=full_name, email=email, paypal_id=paypal_id, username=email) # lets use email as username meanwhile
        mto.set_password(password)
        mto.save(using='vendor_os_db')
        # user = User(email=email, username=email) # let us use email as username meanwhile
        # user.set_password(password)
        # user.save(using='vendor_os_db')
        # MTO.objects.create(full_name=full_name, paypal_id=paypal_id, user=user)
        return