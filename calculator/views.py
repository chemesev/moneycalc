from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Calculator
from .forms import CalculatorForm

@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id = request.user.pk)
    calc = get_object_or_404(Calculator, user_id = request.user.pk)
    #return HttpResponse(calc)
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            add_to_budget = form.cleaned_data['add_to_budget']
            if add_to_budget:
                add_to_budget = add_to_budget
            else:
                add_to_budget = 0

            delete_from_budget = form.cleaned_data['delete_from_budget']
            if delete_from_budget:
                delete_from_budget = delete_from_budget
            else:
                delete_from_budget = 0
            calc.edit_budget(add_to_budget, delete_from_budget)
            calc.save()
            return render(request, 'calculator/thanks.html', {})
    else:
        form = CalculatorForm()
    return render(request, 'calculator/index.html', {
        'form': form,
        'budget': calc.budget
        })
