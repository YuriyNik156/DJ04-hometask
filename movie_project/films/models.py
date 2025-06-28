from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 150, verbose_name = "Название фильма") # переменная verbose_name отображает имя поля в admin.py
    description = models.TextField(verbose_name = "Описание фильма")
    review = models.TextField(verbose_name = "Отзыв")

    def __str__(self):
        return self.title