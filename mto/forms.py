from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from django.forms import TextInput, EmailInput, PasswordInput
# from django import forms
from jobs.models import MTOJobCategory
from .models import MTO

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MTO
        fields = ['username', 'full_name', 'email', 'paypal_id', 'contact_number', 'location', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Middle Last'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'paypal_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PayPal ID'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_mto = True
        user.is_active = True
        user.save(using='vendor_os_db')
        return user

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


job_categories = MTOJobCategory.objects.all()


class MTOUpdateProfileForm(forms.ModelForm):
    job_category = forms.ModelMultipleChoiceField(job_categories, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = MTO
        fields = ['contact_number', 'location', 'paypal_id']
        widgets = {
            'contact_number': forms.NumberInput(attrs={'placeholder': 'Enter contact number', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Location', 'class': 'form-control'}),
            'paypal_id': forms.TextInput(attrs={'placeholder': 'Enter PayPal ID', 'class': 'form-control'}),
        }

#
#
# class SignUpForm(forms.Form):
#     full_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'first middle last'}))
#     email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
#     username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
#     paypal_id = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter paypal ID'}))
#     password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
#     password2 = forms.CharField(
#         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data['email']
#         password = cleaned_data['password']
#         password2 = cleaned_data['password2']
#         if password != password2:
#             raise forms.ValidationError('Passwords did not match', code='invalid password')
#         if User.objects.using('vendor_os_db').filter(username=email).exists():
#             raise forms.ValidationError('A user with that username already exists', code='invalid username')
#         return
#
#     def save(self):
#         cleaned_data = super().clean()
#         full_name = cleaned_data['full_name']
#         email = cleaned_data['email']
#         paypal_id = cleaned_data['paypal_id']
#         password = cleaned_data['password']
#
#         mto = MTO(full_name=full_name, email=email, paypal_id=paypal_id,
#                   username=email)  # lets use email as username meanwhile
#         mto.set_password(password)
#         mto.save(using='vendor_os_db')
#         # user = User(email=email, username=email) # let us use email as username meanwhile
#         # user.set_password(password)
#         # user.save(using='vendor_os_db')
#         # MTO.objects.create(full_name=full_name, paypal_id=paypal_id, user=user)
#         return
