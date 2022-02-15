from django.forms import formset_factory
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Answer, Toko
from .forms import TokoForm, AnswerForm

class Home(ListView):
  model = Toko
  template_name = 'surv/index.html'

  def post(self, request):
    toko_form = TokoForm(request.POST)
    if toko_form.is_valid():
      toko = toko_form.save()
    formset_ans = formset_factory(AnswerForm, extra=2)
    form_ans = formset_ans(request.POST)
    if form_ans.is_valid():
      for form in form_ans:
        if form.is_valid():
          f = form.save()
          f.toko = toko
          f.save()
    return redirect('surv:index')
          

  def get(self, request):
    tokos = Toko.objects.all()
    form_toko = TokoForm()
    form_ans = formset_factory(AnswerForm, extra=2)
    return render(request, self.template_name, {'tokos': tokos, 'form_toko': form_toko, 'form_ans': form_ans})

class Profile(ListView):
  model = Toko
  template_name = 'surv/profile.html'

def your_toko(request):
  tokos = Toko.objects.all() 
  return render(request, 'surv/your_tokos.html', {'tokos': tokos})