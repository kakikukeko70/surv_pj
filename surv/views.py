from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Answer, Toko, Category
from .forms import TokoForm, AnswerForm, CategoryForm
from django import template
register = template.Library()

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
          a = form.save()
          a.toko = toko
          a.save()
    category_form = CategoryForm(request.POST)
    if category_form.is_valid():
      c_text = category_form.cleaned_data['category_text']
      c = Category.objects.get(category_text=c_text)
      c.tokos.add(toko)
    return redirect('surv:index')
          

  def get(self, request):
    tokos = Toko.objects.all()
    categories = Category.objects.all()
    form_toko = TokoForm()
    form_ans = formset_factory(AnswerForm, extra=2)
    return render(request, self.template_name, {'tokos': tokos, 'categories': categories, 'form_toko': form_toko, 'form_ans': form_ans})

class New_category(View):
  template_name = 'surv/new_category.html'
  
  def get(self, request):
    form = CategoryForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request):
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('surv:index')

class Profile(ListView):
  model = Toko
  template_name = 'surv/profile.html'

class Your_toko(ListView):
  model = Toko
  template_name = 'surv/your_tokos.html'  

class Detail(DetailView):
  model = Toko
  template_name = 'surv/detail.html'

class Category_toko_list(DetailView):
  model = Category
  template_name = 'surv/category_toko_list.html'

class Result(DetailView):
  model = Toko
  template_name = 'surv/result.html'

def send(request, toko_id):
  toko = get_object_or_404(Toko, pk=toko_id)
  toko.nsum += 1
  toko.save()
  try:
    selected_answer = toko.answer_set.get(pk=request.POST['answer'])
  except (KeyError, Answer.DoesNotExist):
    return render(request, 'surv/index.html')  
  else:
    selected_answer.num += 1
    selected_answer.save()
    return redirect('surv:index')       