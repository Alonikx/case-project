from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegForm


def main(request):
    return render(request, template_name='caseapp/main.html')


def info_page(request):
    return render(request, template_name='caseapp/info-page.html')


def bron_page(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('afterpayment')
        else:
            raise ValueError('oshibka')

    form = RegForm()
    return render(request, 'caseapp/reg-form.html', {'form': form})


def after_payment(request):
    return render(request, template_name='caseapp/payment-waiting.html')
