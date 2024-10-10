from django import forms
from .models import Item, Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['public_description', 'full_description', 'date_reported', 'location', 'status']
        widgets = {
            'public_description': forms.TextInput(attrs={'placeholder': 'Brief description', 'class': 'form-control'}),
            'full_description': forms.Textarea(attrs={'placeholder': 'Detailed description', 'rows': 4, 'class': 'form-control'}),
            'date_reported': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location where the item was lost/found', 'class': 'form-control'}),
            'status': forms.RadioSelect(choices=[('Lost', 'Lost'), ('Found', 'Found')]),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Add your comment'}),
        }
