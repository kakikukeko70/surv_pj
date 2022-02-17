from pyexpat import model
from django.contrib import admin
from .models import Toko, Answer, Category

admin.site.register(Toko)
admin.site.register(Answer)
admin.site.register(Category)