from django.urls import path
from .views import ReceptsList, RecipeDetail, RecipeCreate, add_comment


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', ReceptsList.as_view(), name='recept_list'), 
   path('<int:pk>', RecipeDetail.as_view(), name='detile_recipe'),
   path('create/', RecipeCreate.as_view(), name='product_create'),
   path('recipe/<int:pk>/comment/', add_comment, name='add_comment')
]