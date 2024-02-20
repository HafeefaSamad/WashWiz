from django import forms
from .models import Account
from django.core.exceptions import ValidationError



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
        fields=('username' ,'email','password','confirm_password') 


# class RegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label="Confirm Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         required=True,
#     )
#     password = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'})
#     )

#     class Meta:
#         model = Account
#         fields = ['username', 'email']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             raise ValidationError("Passwords do not match")

#         if password:
#             if not any(char.isdigit() for char in password):
#                 raise ValidationError("Password must contain at least one digit")
#             if not any(char.isupper() for char in password):
#                 raise ValidationError("Password must contain at least one uppercase letter")
#             if not any(char.islower() for char in password):
#                 raise ValidationError("Password must contain at least one lowercase letter")
#             if not any(char in "!@#$%^&*()" for char in password):
#                 raise ValidationError("Password must contain at least one special character")
#             if len(password) < 8:
#                 raise ValidationError("Password must be at least 8 characters long")

#         return cleaned_data



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

class OtpForm(forms.Form):
    otp = forms.IntegerField()