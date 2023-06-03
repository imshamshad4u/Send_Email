from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

import random


def generate_otp():
    return str(random.randint(100000, 999999))

# def index(request):
#     if request.method == "POST":
#         email=request.POST.get('email')
#         def send_otp_email(email):
#             otp = str(random.randint(100000, 999999))
#             subject = 'OTP Verification'
#             message = f'Your OTP: {otp}'
#             sender_email = 'shamshad.alam@rentokil-pci.com'
#             recipient_email = email

#             send_mail(subject, message, sender_email, [recipient_email])
#     return render(request, "column.html")


# def send_otp_email(email, otp):
#     subject = 'OTP for Registration'
#     message = f'Your OTP: {otp}'
#     sender_email = 'shamshad.alam@rentokil-pci.com'
#     recipient_email = email

#     send_mail(subject, message, sender_email, [recipient_email])
def send_email(email):
    subject = 'Email verification'
    # message = f'Activate your email account : {email}'
    sender_email = 'shamshad.alam@rentokil-pci.com'
    recipient_email = email
    context = {
        'name': 'shamshad',
        # 'link':'https://chat.openai.com/'
        'link': 'https://8000-cs-172903303916-default.cs-asia-southeast1-bool.cloudshell.dev/'
    }
    html_message = render_to_string('send_email.html', context)
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, sender_email, [
              recipient_email], html_message=html_message)


def register(request):
    if request.method == 'POST':
        # Retrieve form data
        email = request.POST.get('email')
        # Add more form fields as needed

        # Generate OTP
        # otp = generate_otp()

        # # Send OTP via email
        # send_otp_email(email, otp)
        send_email(email)

        # Store OTP in the session or database for later validation
        # request.session['registration_otp'] = otp

        # Redirect to OTP verification page
        # return redirect('otp_verification')
        return HttpResponse(f'email sent on registered email id:{email}')

    return render(request, 'column.html')

# def home(request):
#     return HttpResponse("this is home page ")


def otp_verification(request):
    if request.method == 'POST':
        # Retrieve entered OTP from the form
        entered_otp = request.POST.get('otp')

        # Retrieve stored OTP from the session or database
        stored_otp = request.session.get('registration_otp')

        if entered_otp == stored_otp:
            # OTP is valid, proceed with registration or desired action
            # Add your registration logic here or perform the desired action
            print('success')
            # Clear the OTP from the session
            del request.session['registration_otp']

            # Redirect to success page or perform further actions
            # return redirect('registration_success')
            return HttpResponse('success!!!')
        else:
            # OTP is invalid, display an error message or take appropriate action
            # Add your error handling logic here
            return HttpResponse("failure")
    return render(request, 'otp_verification.html')
