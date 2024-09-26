from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Recept, Author


class ReceptsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Recept
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'date_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'recepts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'recepts'
    
    
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context
    
class RecipeDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Recept
    # Используем другой шаблон — product.html
    template_name = 'recipe.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'recipe'
    
@method_decorator(login_required, name='dispatch')
class RecipeCreate(CreateView):
    model = Recept
    template_name = 'create.html'
    fields = ['title', 'text', 'ccal']
    success_url = reverse_lazy('recept_list') # Укажите URL для перенаправления после успеха

    def form_valid(self, form): 
        author, created = Author.objects.get_or_create(author_user=self.request.user)  # Используйте author_user
        form.instance.author = author
        return super().form_valid(form)