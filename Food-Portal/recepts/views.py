from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from .models import Recept, Author, Comment
from .forms import CommentForm
from .filtrs import ProductFilter


class ReceptsList(ListView):
    model = Recept
    ordering = 'date_creation'
    template_name = 'recepts.html'
    context_object_name = 'recepts'
    paginate_by = 9
    
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = ProductFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    
class RecipeDetail(DetailView):
    form_class = CommentForm
    model = Recept
    template_name = 'recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(commentRecept=self.object)
        return context

@login_required
def add_comment(request, pk):
    recipe = Recept.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commentRecept = recipe
            comment.commentUser = request.user
            comment.save()
            return redirect('detile_recipe', pk=recipe.pk)

    return redirect('detile_recipe', pk=recipe.pk)
    
@method_decorator(login_required, name='dispatch')
class RecipeCreate(CreateView):
    model = Recept
    template_name = 'create.html'
    fields = ['title', 'text', 'ccal']
    success_url = reverse_lazy('recept_list')

    def form_valid(self, form): 
        author, created = Author.objects.get_or_create(author_user=self.request.user)  # 
        form.instance.author = author
        return super().form_valid(form)
    

