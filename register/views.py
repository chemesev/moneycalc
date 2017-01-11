from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import RegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] and form.cleaned_data['password2']:
                if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                    user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                    )
                    user.save()
            return HttpResponse('Registered')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
