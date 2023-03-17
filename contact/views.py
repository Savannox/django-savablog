from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from contact.forms import ContactForm
from blog.settings import EMAIL_HOST_USER
from django.urls import reverse

# Create your views here.

def ContactView(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            email_sended = EmailMessage(
                'SavaBlog: Nuevo mensaje de contacto',
                f'De {name} <{email}>\n\nEscribio:\n{message}',
                EMAIL_HOST_USER,
                ['ivankunstler2016@gmail.com'],
                reply_to=[email]
            )
        try:
            email_sended.send()
            return redirect(reverse('contact') + '?ok')
        except:
            return redirect(reverse('contact') + '?fail')
    return render(request, 'contact/contacto.html', {
        'form':form
    })
    