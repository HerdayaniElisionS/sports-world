from django.urls import path
from .views import show_info

app_name = 'main'

urlpatterns = [
    path('', show_info, name='show_info'),  
    path('info/', show_info, name='show_info_info'),  
]
