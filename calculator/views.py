from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Calculator
from .forms import CalculatorForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            add_to_budget = form.cleaned_data.get('add_to_budget')
            delete_from_budget = form.cleaned_data.get('delete_from_budget')
            if not add_to_budget:
                add_to_budget = 0
            if not delete_from_budget:
                delete_from_budget = 0
            calc.edit_budget(add_to_budget, delete_from_budget)
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        form = CalculatorForm()
    return render(request, 'calculator/index.html', {
        'form': form,
        'budget': calc.budget
        })


def base(request):
    return render(request, 'calculator/base.html', {})
