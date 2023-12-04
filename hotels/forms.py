from  django import forms
from .models import Hotel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy

class HotelForms(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'rate']

    name = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
    rate = forms.CharField(max_length=200)

    # class SurveyForms(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_action = reverse_lazy('home')
    #     self.helper.form_method = 'POST'
    #     self.helper.add_input(Submit('submit', 'Submit'))
