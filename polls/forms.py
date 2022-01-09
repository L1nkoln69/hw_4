from django import forms

from .models import Person


class Triangle(forms.Form):
    cathetus_1 = forms.DecimalField(label='Катет 1')
    cathetus_2 = forms.DecimalField(label='Катет 2')

    def clean_cathetus_1(self):
        cathetus_1 = self.cleaned_data.get('cathetus_1')
        if cathetus_1 < 0:
            raise forms.ValidationError('неправильоне значение')
        else:
            return cathetus_1

    def clean_cathetus_2(self):
        cathetus_2 = self.cleaned_data.get('cathetus_2')
        if cathetus_2 < 0:
            raise forms.ValidationError('неправильоне значение')
        else:
            return cathetus_2


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]
