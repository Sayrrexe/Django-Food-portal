from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Recept, Author


class ReceptsList(ListView):
    model = Recept
    ordering = 'date_creation'
    template_name = 'recepts.html'
    context_object_name = 'recepts'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context
    
class RecipeDetail(DetailView):
    model = Recept
    template_name = 'recipe.html'
    context_object_name = 'recipe'
    
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
    