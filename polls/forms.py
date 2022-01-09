from django import forms

from .models import Person


class Triangle(forms.Form):
    Cathetus_1 = forms.DecimalField(label='Катет 1')
    Cathetus_2 = forms.DecimalField(label='Катет 2')

    def new_athetus_1(self):
        Cathetus_1 = self.cleaned_data.get('Cathetus_1')
        if Cathetus_1 < 0:
            raise forms.ValidationError('неправильоне значение')
        else:
            return Cathetus_1

    def new_athetus_2(self):
        Cathetus_2 = self.cleaned_data.get('Cathetus_2')
        if Cathetus_2 < 0:
            raise forms.ValidationError('неправильоне значение')
        else:
            return Cathetus_2


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]
