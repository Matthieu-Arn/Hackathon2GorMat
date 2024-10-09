from django import forms
from .models import Item, Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['public_description', 'full_description', 'date_reported', 'location', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
