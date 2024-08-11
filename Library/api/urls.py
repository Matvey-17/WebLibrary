from django.urls import path
from Library.api.views import ListBookView, AddBookView, RemoveBookView, ListMyBookView, ListDebtorsView

app_name = 'Library'

urlpatterns = [
    path('list_book/', ListBookView.as_view(), name='list_book'),
    path('list_my_book/', ListMyBookView.as_view(), name='list_my_book'),
    path('list_debtors/', ListDebtorsView.as_view(), name='list_debtors'),
    path('add_book/<int:book_id>/', AddBookView.as_view(), name='add_book'),
    path('remove_book/<int:book_id>/', RemoveBookView.as_view(), name='remove_book')
]
