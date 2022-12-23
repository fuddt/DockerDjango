from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re


class MessageForm(forms.ModelForm):
    class Meta:
        model = AllMessage
        fields = ['name','message']
        widget = {
            'message': forms.Textarea(attrs={
                                             "class":"form-control",
                                             "placeholder":"Username",
                                             "aria-label":"Username",
                                             "aria-describedby":"addon-wrapping"
                                             })
        }
        labels = {
            'name' : '名前',
            'message' : 'メッセージ'
        }