from django import forms
from . import models
class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ('text',)
        widgets = {
            'text':
            forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title','message',)
        widgets = {
            'title':forms.TextInput(attrs={'class': 'editable medium-editor-textinput postcontent'}),
            'message': forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'})
        }

