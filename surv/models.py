from django.db import models

class Toko(models.Model):
  text = models.CharField(blank=False, null=True, max_length=140)
  nsum = models.IntegerField(default=0)

  def __str__(self):
    return self.text

class Answer(models.Model):
  answer = models.CharField(blank=True, null=True, max_length=12)
  num = models.IntegerField(default=0, null=True)
  toko = models.ForeignKey(Toko, null=True, on_delete=models.CASCADE)

  def __str__(self):
    if self.answer == None:
      return "ERROR-CUSTOMER Answer IS NULL"
    return self.answer

class Category(models.Model):
  category_text = models.CharField(blank=False, max_length=10)
  tokos = models.ManyToManyField(Toko)

  def __str__(self):
    return self.category_text