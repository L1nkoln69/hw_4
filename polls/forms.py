from django import forms


class Triangle(forms.Form):
    Cathetus_1 = forms.FloatField(label='Катет первый')
    Cathetus_2 = forms.FloatField(label='Катет второй')
    Hypotenuse = None
