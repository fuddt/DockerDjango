from django.test import TestCase

# Create your tests here.

import inspect
# formクラスのobjectの確認
from django import forms

for class_name in inspect.getmembers(forms, inspect.isclass):
    print(class_name[0])
