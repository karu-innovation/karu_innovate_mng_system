from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    widget = {
        'email':forms.EmailInput(attrs={'class':'form-control'})
    }
    
class TextForm(forms.Form):
    text = forms.CharField()
    widget = {
        'text':forms.TextInput(attrs={'class':'form-control'})
    }