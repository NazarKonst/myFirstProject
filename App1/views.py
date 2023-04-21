from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

full_name = {'full_name': 'Константинов Н.В.'}

about_info = {'just_name': 'Назар', 'surname': 'Константинов', 'batyname': 'Вячеславович', 'phone_number': '53-54-77', 'email': 'gwenardell@ya.ru'}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def hello(request):
    return render(request, 'main.html', full_name)


def about(request):
    return render(request, 'about.html', about_info)


def fu_item(request, id_num):
    for i in range(len(items)):
        if id_num == items[i]["id"]:
            return render(request, 'item.html', {'item': items[i]})
    return render(request, 'item_not_found.html', {'item': items[i]})


def fu_items(request):
    return render(request, 'items.html', {'items': items})
