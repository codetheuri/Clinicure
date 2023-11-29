# premium/views.py
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .forms import PremiumSubscriptionForm, CustomForm
from .models import PremiumSubscription
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template

def subscribe_premium(request):
    if request.method == 'POST':
        form = PremiumSubscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('premium:subscribers')
    else:
        form = PremiumSubscriptionForm()

    return render(request, 'subscribe.html', {'form': form})
def premium_users(request):
    view = PremiumSubscription.objects.all()
    return render(request, 'subscribers.html', {'subscriber': view})

def update_subscription(request, id):
    subscription = get_object_or_404(PremiumSubscription, id=id)

    if request.method == 'POST':
        form = PremiumSubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('premium:subscribers')
    else:
     form = PremiumSubscriptionForm(instance=subscription)
     return render(request, 'update_subscription.html', {'form': form, 'subscription': subscription})

def delete_subscription(request, id):
    subscription = get_object_or_404(PremiumSubscription, id=id)
    if request.method =='POST':
        subscription.delete()
        return redirect('premium:subscribers')
    return render(request, 'delete_subscription.html', {'subscription':subscription})
def sendtoemail(request):
    subcribers= PremiumSubscription.objects.all()
    for subcribers in subcribers:
        print(subcribers.patient)
        email_address = subcribers.email

        message = 'Did you know that sunlight supplies vitamin D'

        subject = 'Clinicure Health facts'
        context = {'name': subcribers.patient, 'message': message}
        message = render_to_string('email.html',context)
        email = EmailMessage(subject, message, "clinicure", [email_address])
        email.content_subtype = "html"
        email.send()

    return render(request, 'success.html')


def custom_message(request):
       if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            status = form.cleaned_data['status']
            subject = form.cleaned_data['subject']
            print(message)

            # sending  email
            if status == 'all':
                premium = PremiumSubscription.objects.all()
            else:
                premium = PremiumSubscription.objects.filter(status=status)
            print(premium)
            for premium in premium:
                print(premium.patient)
                email_address = premium.email
                context = {'name': premium.patient, 'message': message}
                email_template = get_template('email.html').render(context)
                email = EmailMessage(subject, email_template, "clinicure Clinic Health facts", [email_address])
                email.content_subtype = "html"
                email.send()
            return redirect('premium:custom_message')
        else:
            print(form.errors)
       return render(request, 'message.html')
