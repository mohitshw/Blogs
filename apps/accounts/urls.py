from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_step_one, name='signup'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('signup-step-two/', views.signup_step_two, name='signup_step_two'),
    path('signin/', views.signin, name='signin'),
    path('verify-signin-otp/', views.verify_signin_otp, name='verify_signin_otp'),
]