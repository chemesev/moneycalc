from django import forms

class CalculatorForm(forms.Form):
        add_to_budget = forms.DecimalField(max_digits=12, decimal_places=2, required=False)
        delete_from_budget = forms.DecimalField(max_digits=12, decimal_places=2, required=False)
