from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
    label="Password",

    widget=forms.PasswordInput(
        attrs={'placeholder':'Enter Password', 'class':'form-control'}
    )
)

    class Meta:
        model = Account
        fields=('email','password','username','confirm_password') 

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class ForgotForm(forms.Form):
    email = forms.EmailField()

class ResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta :
        model = Account
        fields = ['first_name','last_name','city','Phone_number']

        