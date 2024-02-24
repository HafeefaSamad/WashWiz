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
        fields = ('username', 'email', 'password', 'confirm_password') 



# class RegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(
#         label="Confirm Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#         required=True,
#     )
#     password = forms.CharField( 
#         label="Password",
#         widget=forms.PasswordInput(
#             attrs={'placeholder':'Enter Password', 'class':'form-control'}
#         )
#     )
    
#     class Meta:
#         model = Account
#         fields = ('username', 'email', 'password', 'confirm_password') 
        
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if not any(char.isupper() for char in password):
#             raise ValidationError('Password must contain at least one uppercase letter')
#         if not any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
#             raise ValidationError('Password must contain at least one special character')
#         if len(password) >6 :
#             raise ValidationError('Password length must be at least 6 characters')
#         return password

#     def clean(self):
#         cleaned_data = super().clean()
#         print(cleaned_data, '5555555555555555555555555555')
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
        
#         if password != confirm_password:
#             raise ValidationError({'confirm_password': 'Passwords do not match'})
        
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