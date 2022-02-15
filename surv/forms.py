from django.forms import ModelForm
from .models import Toko, Answer

class TokoForm(ModelForm):
  class Meta:
    model = Toko
    fields = ['text']

class AnswerForm(ModelForm):
  class Meta:
    model = Answer
    fields = ['answer']