


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm,ForgotForm, ResetForm, UserProfileForm, OtpForm
from apps.accounts.models import Account
from django.conf import settings
from django.core.mail import send_mail
import pyotp


def Register(request):
    
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Account.objects.create_user(email=email,password=password,username=username)
            user.save()

            subject='Car wash'
            totp = pyotp.TOTP(pyotp.random_base32())
            otp = totp.now()
            request.session['generated_otp'] = otp 
            message=f'Your registeration otp is {otp} '
            recipient=user.email
            print(otp, recipient)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
            # return redirect('login')
            return redirect('otp',user.id)
        else:
            messages.error(request, "Please Correct Below Errors")
           
    else:
        form = RegistrationForm()   
        
    return render(request, 'register.html', {'registration_form':form})

def login_user(request):
    if request.method == 'POST': 
        form=LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password.')
            else:
                messages.error(request, 'Form is not valid.') 

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        return redirect('login')
    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = Account.objects.get(email=email)
                print(user.id)
                messages.success(request, 'Password reset email sent successfully.')
                return redirect('reset', id=user.id)
            except Account.DoesNotExist:
                messages.error(request, 'Account with this email does not exist.')
    else:
        form = ForgotForm()
    return render(request, 'forgotpassword.html', {'form': form})

def reset_password(request, id):
    user = Account.objects.get(id=id)
    print('hai', user)
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmpassword = form.cleaned_data.get('confirmpassword')
            if password and confirmpassword and password != confirmpassword:
                raise form.ValidationError('password is not match')
            else:
                user.set_password(password)
                user.save()
                return redirect('login')
    else:
        form =ResetForm()
    return render(request, 'reset.html', {'form': form})


def userprofile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            Account.objects.update(
                first_name=form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                city = form.cleaned_data.get('city'),
                Phone_number = form.cleaned_data.get('Phone_number'),

            )
        
            form.save()
    else:
        form = UserProfileForm(instance=user) 
    return render(request, 'home/userprofile.html', {"form": form})

def Verify_otp(request, id):
    user = Account.objects.get(id=id)
    otp = request.session.get('generated_otp')
    print(type(otp),'sdefsdf')
    if request.method == "POST":
        form = OtpForm(request.POST)
        if form.is_valid():
            otp_input = form.cleaned_data.get('otp')
            print(type(otp_input), "sdflkbfk")
            print(otp == otp_input)
            if otp == str(otp_input):
                user.is_active = True  
                user.save()
                messages.success(request, 'Your Account is Activated, now you can Login.')
                return redirect('login')  
            else:
                messages.error(request, 'Invalid otp, Please try again.')
                return redirect('otp', id=id) 
    else:
        form = OtpForm()
        return render(request, 'otp.html', {'form': form})
    




    
    

                


     

