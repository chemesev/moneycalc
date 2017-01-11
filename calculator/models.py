import decimal

from django.db import models
from django.contrib.auth.models import User


class Calculator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def edit_budget(self, add_to_budget, decrease_of_budget):
        self.budget += add_to_budget
        self.budget -= decrease_of_budget
        return self.budget
    def __str__(self):
        return "{}'s budget".format(self.user)
