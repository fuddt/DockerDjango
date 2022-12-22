from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.
def name_validator(value):
    if re.search(r'[0-9]',value):
        raise ValidationError("sorry, not use numbers for 'name'")

class AllMessage(models.Model):
    name = models.CharField(max_length=20, validators=[name_validator])
    message = models.TextField(max_length=400)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'名前は{self.name}。\
                メッセージは「{self.message}」です。\
                投稿日時:{self.datetime}'
        