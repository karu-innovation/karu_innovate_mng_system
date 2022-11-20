from django import forms
from .models import Events

class CreateEventForm(forms.ModelForm):
    class Meta:
        model=Events
        fields=['name','image','description','file','category','venue','location','community']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'file':forms.FileInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'venue':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'community':forms.Select(attrs={'class':'form-control'}),
        }