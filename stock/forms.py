from django import forms
from .models import Investors


class UserInputFormSales(forms.Form):
    user_input = forms.CharField(label='Enter number of timber to predict the sales',
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 label_suffix="")


class UserInputFormProfit(forms.Form):
    user_input = forms.CharField(label='Enter sales value to predict the profit',
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 label_suffix="")


class UserInputFormDemand(forms.Form):
    user_input = forms.CharField(label='Enter supply value to predict the demand',
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                 label_suffix="")


class InvestorsForm(forms.ModelForm):
    amount = forms.DecimalField(label='Amount to Invest', widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label_suffix="")

    class Meta:
        model = Investors
        fields = ('amount',)


