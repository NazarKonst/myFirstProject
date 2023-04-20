from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

full_name = 'Константинов Н.В.'
just_name = 'Назар'
just_surname = 'Константинов'
batyname = 'Вячеславович'
phone_number = '53-54-77'
email = 'gwenardell@ya.ru'

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def hello(request):
    return HttpResponse(f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{full_name}</i>
    """)


def about(request):
    return HttpResponse(f"""
    <p>Имя: <b>{just_name}</b></p>
    <p>Отчество: <b>{batyname}</b></p>
    <p>Фамилия: <b>{just_surname}</b></p>
    <p>Телефон: <b>{phone_number}</b></p>
    <p>Email: <b>{email}</b></p>
    """)


def fu_item(request, id_num):
    for i in range(len(items)):
        if id_num == items[i]["id"]:
            return HttpResponse(f"""
                <!DOCTYPE html>
                <html>
                  <head>
                    <title>Товар и количество</title>
                  </head>
                  <body>
                    <h1>{items[i]["name"]}, {items[i]["quantity"]} шт.</h1>
                  </body>
                </html>
                """)

    return HttpResponse(f"""
        <h1>Товар с id = {id_num} не найден</h1>
        """)


def fu_items(request):
    return render(request, 'main.html', {'items': items})
