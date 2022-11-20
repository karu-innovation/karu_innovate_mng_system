from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField(max_length=100)
    widget = {
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'message':forms.Textarea(attrs={'class':'form-control'}),
        'subject':forms.TextInput(attrs={'class':'form-control'})
    }
    
class TextForm(forms.Form):
    text = forms.CharField()
    widget = {
        'text':forms.TextInput(attrs={'class':'form-control'})
    }