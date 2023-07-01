from django import forms
from .models import Comment
from .models import Club

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        from django import forms
from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'introduction', 'number']

