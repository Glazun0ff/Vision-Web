from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Elements


def index(request):
    elements = Elements.objects.all()
    return render(request, 'landing/index.html', {'elements': elements})


def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail('Subject', message, 'no-reply@app.com', [email], fail_silently=False)
        # return HttpResponse("Письмо отправлено на " + email)
        messages.add_message(request, messages.INFO, 'Письмо отправлено на ' + email)
    return render(request, 'landing/send_email.html')


class AllUsersView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        all_users = User.objects.values()
        return Response({'all_users': all_users})
