from audioop import reverse
from django.http import HttpResponseRedirect
from multiprocessing import context
from django.forms import formset_factory, modelformset_factory
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Answer, Toko
from .forms import TokoForm, AnswerForm

class Home(View):
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

class Detail(DetailView):
  model = Toko
  template_name = 'surv/detail.html'

def send(request, toko_id):
  toko = get_object_or_404(Toko, pk=toko_id)
  selected_answer = toko.answer_set.get(pk=request.POST['answer'])
  selected_answer.num += 1
  selected_answer.save()
  return HttpResponseRedirect(reverse('surv:index'))


class Profile(ListView):
  model = Toko
  template_name = 'surv/profile.html'

class Your_toko(ListView):
  model = Toko
  template_name = 'surv/your_tokos.html'