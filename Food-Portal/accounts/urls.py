from django.urls import path
from .views import ProfileView, profile


urlpatterns = [
   path('<int:pk>', ProfileView.as_view(), name='profile'), 
   path('', ProfileView.as_view(), name='profile')
]