from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
#     path('', views.quote, name='quote'),
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag')
]
