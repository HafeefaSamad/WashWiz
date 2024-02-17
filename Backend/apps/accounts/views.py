


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm,LoginForm,ForgotForm, ResetForm, UserProfileForm
from apps.accounts.models import Account
from django.core.exceptions import ObjectDoesNotExist


def Register(request):
    context = {}
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password')
            user = Account.objects.create_user(email=email,password=raw_pass,username=username)
            user.save()
            return redirect('login')
        else:
            messages.error(request, "Please Correct Below Errors")
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

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
                messages.error(request, 'Form is not valid.')  # Handle invalid form submission

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        return redirect('login')
    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

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
        form = UserProfileForm(instance=user)  # Populate the form with existing user data
    return render(request, 'home/userprofile.html', {"form": form})

                


     

