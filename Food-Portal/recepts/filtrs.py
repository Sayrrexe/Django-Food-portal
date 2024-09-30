from django_filters import FilterSet
from .models import Recept


class ProductFilter(FilterSet):
   class Meta:

       model = Recept

       fields = {
           # поиск по названию
           'title': ['icontains'],
           'ccal': [
               'lt',  
               'gt',  
           ],
       }