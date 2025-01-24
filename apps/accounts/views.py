from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupStepOneForm, OTPForm, SignupStepTwoForm
from .models import CustomUser
import random
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.db import transaction

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    send_mail(
        'Your OTP',
        f'Your OTP is: {otp}',
        'from@example.com',
        [email],
        fail_silently=False,
    )

@transaction.atomic
def signup_step_one(request):
    if request.method == 'POST':
        form = SignupStepOneForm(request.POST)
        if form.is_valid():
            # Generate temporary username to satisfy unique constraint
            temp_username = f"temp_{random.randint(10000, 99999)}"
            
            # Create user with temporary username
            user = CustomUser.objects.create(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                username=temp_username
            )
            
            # Generate and save OTP
            otp = generate_otp()
            user.otp = otp
            user.otp_created_at = timezone.now()
            send_otp_email(user.email, otp)
            user.save()
            
            request.session['signup_email'] = user.email
            return redirect('verify_otp')
    else:
        form = SignupStepOneForm()
    return render(request, 'signup_step_one.html', {'form': form})

def signup_step_two(request):
    email = request.session.get('signup_email')
    if not email:
        return redirect('signup')

    if request.method == 'POST':
        form = SignupStepTwoForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(email=email)
            
            # Update username
            new_username = form.cleaned_data['username']
            # Check if username already exists
            if CustomUser.objects.filter(username=new_username).exists():
                return render(request, 'signup_step_two.html', {
                    'form': form, 
                    'error': 'Username already exists'
                })
            
            user.username = new_username
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupStepTwoForm()
    return render(request, 'signup_step_two.html', {'form': form})

# Rest of the views remain the same


def verify_otp(request):
    email = request.session.get('signup_email')
    if not email:
        return redirect('signup')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(email=email)
            otp_sent_time = user.otp_created_at
            
            # Check OTP expiry (15 minutes)
            if timezone.now() > otp_sent_time + timedelta(minutes=15):
                return render(request, 'verify_otp.html', {'form': form, 'error': 'OTP expired'})
            
            if form.cleaned_data['otp'] == user.otp:
                return redirect('signup_step_two')
            else:
                return render(request, 'verify_otp.html', {'form': form, 'error': 'Invalid OTP'})
    else:
        form = OTPForm()
    return render(request, 'verify_otp.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            otp = generate_otp()
            user.otp = otp
            user.otp_created_at = timezone.now()
            send_otp_email(email, otp)
            user.save()
            request.session['signin_email'] = email
            return redirect('verify_signin_otp')
        except CustomUser.DoesNotExist:
            return render(request, 'signin.html', {'error': 'Email not found'})
    return render(request, 'signin.html')

def verify_signin_otp(request):
    email = request.session.get('signin_email')
    if not email:
        return redirect('signin')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(email=email)
            otp_sent_time = user.otp_created_at
            
            # Check OTP expiry (15 minutes)
            if timezone.now() > otp_sent_time + timedelta(minutes=15):
                return render(request, 'verify_signin_otp.html', {'form': form, 'error': 'OTP expired'})
            
            if form.cleaned_data['otp'] == user.otp:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'verify_signin_otp.html', {'form': form, 'error': 'Invalid OTP'})
    else:
        form = OTPForm()
    return render(request, 'verify_signin_otp.html', {'form': form})