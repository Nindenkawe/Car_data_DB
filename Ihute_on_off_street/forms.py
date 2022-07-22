from time import time
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subscriber, Proposed_insucovers, Transaction
from django import forms
from django.forms import ModelForm


class Registration_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class rqst_chauffeur(ModelForm):
    phone_number = forms.IntegerField(required=True)
    location = forms.CharField(required=True)
    time = forms.TimeField(required=True)
    
    class Meta:
        model = Subscriber
        fields =  ['phone_number','location','time']


class buy_insurance(ModelForm):
    class Meta:
        model = Proposed_insucovers
        fields = "__all__"