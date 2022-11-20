from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    widget = {
        'email':forms.EmailInput(attrs={'class':'form-control'})
    }