from django.shortcuts import render
import requests as request_server


def index(request):
    return render(request, 'index.html')


def catalog(request):
    cookies = request.COOKIES
    response = request_server.get('http://localhost:8000/api/list_book/', cookies=cookies)
    if response.status_code == 200:
        books = response.json()['detail']
    else:
        books = []

    return render(request, 'catalog.html', {'books': books})


def catalog_my_book(request):
    cookies = request.COOKIES
    response = request_server.get('http://localhost:8000/api/list_my_book/', cookies=cookies)
    if response.status_code == 200:
        books = response.json()['detail']
    else:
        books = []

    return render(request, 'my_books.html', {'books': books})


def list_debtors(request):
    cookies = request.COOKIES
    response = request_server.get('http://localhost:8000/api/list_debtors/', cookies=cookies)
    if response.status_code == 200:
        debtors = response.json()['detail']
    else:
        debtors = []

    return render(request, 'debtors.html', {'debtors': debtors})
