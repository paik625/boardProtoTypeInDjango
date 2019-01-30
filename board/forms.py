from django.contrib.auth.models import User
from django import forms


# class createForm(forms.ModelForm):
#     title = forms.CharField(label='Password', widget=forms.PasswordInput)
#     author = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
#     author = forms.TextField(null=False, max_length=20)
#     title = forms.TextField(null=False)
#     content = forms.TextField(null=False)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name','last_name', 'email']
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords not matched!')
#         return cd['password2']