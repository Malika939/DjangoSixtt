from django.urls import path

from .views import *


urlpatterns = [
    path('', main),
    path('category/<int:category_id>', get_category),
]


