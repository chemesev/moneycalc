from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Calculator, BudgetExpenses, BudgetIncome
from .forms import CalculatorForm, ExpensesForm, IncomeForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
    expenses = BudgetExpenses.objects.all()
    income = BudgetIncome.objects.all()
    inc_form = IncomeForm()
    exp_form = ExpensesForm()
    return render(request, 'calculator/index.html', {
        'inc_form': inc_form,
        'exp_form': exp_form,
        'budget': calc.budget,
        'expenses': expenses,
        'income': income,
        })


def base(request):
    return render(request, 'base.html', {})


def add_budget(request):
    if request.method == 'POST':
        calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
        inc_form = IncomeForm(request.POST)
        if inc_form.is_valid():
            value = inc_form.cleaned_data.get('value')
            changes = BudgetIncome(
                calculator=calc,
                value=value,
                category=inc_form.cleaned_data.get('category'),)
            changes.save()
            calc.edit_budget(value, 0)
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        HttpResponseRedirect(reverse('calculator:budget_edit'))
    return HttpResponseRedirect(reverse('calculator:budget_edit'))


def del_budget(request):
    if request.method == 'POST':
        calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
        exp_form = ExpensesForm(request.POST)
        if exp_form.is_valid():
            value = exp_form.cleaned_data.get('value')
            changes = BudgetExpenses(
                calculator=calc,
                value=value,
                category=exp_form.cleaned_data.get('category'),)
            calc.edit_budget(0, value)
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        HttpResponseRedirect(reverse('calculator:budget_edit'))
    return HttpResponseRedirect(reverse('calculator:budget_edit'))

# calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
# if request.method == 'POST':
#     if 'budget_add' in request.POST:
#         inc_form = IncomeForm(request.POST, prefix='income')
#         if inc_form.is_valid():
#             value = inc_form.cleaned_data.get('value')
#             changes = BudgetIncome(
#                 calculator=calc,
#                 value=value,
#                 category=form.cleaned_data.get('category'),)
#             calc.edit_budget(value, 0)
#             calc.save()
#             return HttpResponseRedirect(reverse('calculator:budget_edit'))
#
#     form = IncomeForm = CalculatorForm(request.POST)
#     if form.is_valid():
#         add_to_budget = form.cleaned_data.get('add_to_budget')
#         delete_from_budget = form.cleaned_data.get('delete_from_budget')
#         if not add_to_budget:
#             add_to_budget = 0
#         if not delete_from_budget:
#             delete_from_budget = 0
#         calc.edit_budget(add_to_budget, delete_from_budget)
#         calc.save()
#         return HttpResponseRedirect(reverse('calculator:budget_edit'))
# else:
#     form = CalculatorForm()
