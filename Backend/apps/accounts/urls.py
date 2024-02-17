from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('forgot/', views.forgot_password, name='forgot'),
    path('reset/<int:id>/', views.reset_password, name='reset'),
    path('userprofile/', views.userprofile, name='profile'),


]
