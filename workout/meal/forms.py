from django import forms


class MealFrom(forms.Form):
    amount = forms.IntegerField()
    

