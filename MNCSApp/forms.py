from django import forms
from django.forms.widgets import Widget
from django.core.validators import RegexValidator

class ValidateFrm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(min_length=6,required= True,widget=forms.PasswordInput)
    dob=forms.DateField()
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,12}$',message="Phone numb er must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone = forms.CharField(validators=[phone_regex],
    max_length=17,required= True,widget=forms.NumberInput)
