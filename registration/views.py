from re import template
from django.views.generic import TemplateView

class Index(TemplateView):
  template_name = 'registration/index.html'