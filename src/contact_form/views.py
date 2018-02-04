from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render

from decouple import config

from .forms import ContactForm


def send_email(from_email, to_emails, subject, message):
    headers = {'Reply-To': from_email, 'From': 'contact form'}
    email = EmailMessage(subject, message, to=to_emails,
                         headers=headers)
    email.send()


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            domain = get_current_site(request)
            from_email = form.cleaned_data['from_email']
            to_emails = [settings.CONTACT_FORM_EMAIL]
            subject = '{} contact form'.format(domain)
            message = form.cleaned_data['message']
            send_email(from_email, to_emails, subject, message)
            messages.success(request, 'Message sent!')
        else:
            messages.warning(request, 'There was a problem! Please try again.')

    form = ContactForm
    template = 'contact_form/contact_page.html'
    context = {'form': form, 'description': settings.CONTACT_PAGE_DESCRIPTION}
    return render(request, template, context)
