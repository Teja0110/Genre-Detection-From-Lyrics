from django.urls import path
from GenrePrediction import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpage/',  views.new_page,  name="my_function"),
]