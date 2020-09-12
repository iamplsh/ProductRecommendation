from django.urls import path

from .views import index, list_of_recommendations

urlpatterns = [

    path('', index),
    path('recommend/Stuff', list_of_recommendations),
]