from pyexpat import model
from django.forms import ModelForm
from .models import Toko, Answer, Category

class TokoForm(ModelForm):
  class Meta:
    model = Toko
    fields = ['text']

class AnswerForm(ModelForm):
  class Meta:
    model = Answer
    fields = ['answer']

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = ['category_text']