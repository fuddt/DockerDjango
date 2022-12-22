from django.test import TestCase
from django import forms
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
import re
from .models import *
from .forms import *
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView
from django.core.paginator import Paginator
# Create your tests here.

class TestForm(TestCase):
    def test_was_print_Form_as_table_method(self):
        f = MessageForm()
        print(f.as_table())