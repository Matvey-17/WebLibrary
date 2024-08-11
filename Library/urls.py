from django.urls import path
from .views import index, catalog, catalog_my_book, list_debtors

app_name = 'Library'

urlpatterns = [
    path('', index, name='main'),
    path('catalog', catalog, name='catalog'),
    path('my_book', catalog_my_book, name='my_book'),
    path('debtors', list_debtors, name='debtors')
]