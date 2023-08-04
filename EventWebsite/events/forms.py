from django import forms

from events.models import event

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields=['image', 'event_name','user_id','location','data']

        widgets ={
            'image':forms.FileInput(attrs ={'class':'form-control'}),
            'event_name':forms.TextInput(attrs ={'class':'form-control'}),
            'user_id':forms.TextInput(attrs ={'class':'form-control'}),
            'location':forms.Select(attrs={'class':'form-control'}),
            'data':forms.Textarea(attrs ={'class':'form-control'}),
        }
        