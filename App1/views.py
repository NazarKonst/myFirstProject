from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Item

# Create your views here.
from django.http import HttpResponse

full_name = {'full_name': 'Константинов Н.В.'}

about_info = {'just_name': 'Назар', 'surname': 'Константинов', 'batyname': 'Вячеславович', 'phone_number': '53-54-77',
              'email': 'gwenardell@ya.ru'}


# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124},
# ]

# first_item = Item(id=1, name="Кроссовки", brand="abibas", count=5)
# first_item.save()

def hello(request):
    return render(request, 'main.html', full_name)


def about(request):
    return render(request, 'about.html', about_info)


def fu_items(request):
    context = {}
    result = []
    queryset = Item.objects.all()
    for el in queryset:
        answer = {'id': el.id, 'name': el.name, 'brand': el.brand, 'count': el.count, 'description': el.description}
        result.append(answer)
    context['items'] = result
    return render(request, 'items.html', context)


# def fu_item(request, id_num):
#     item = get_object_or_404(Item, id=id_num)
#     return render(request, 'item.html', {'item': item})

def fu_item(request, id_num):
    try:
        item = Item.objects.get(id=id_num)
    except Item.DoesNotExist:
        return render(request, 'item_not_found.html', {'item': id_num})
    return render(request, 'item.html', {'item': item})


@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        item_name = request.POST.get('name')
        item_brand = request.POST.get('brand')
        item_count = request.POST.get('count')
        item_description = request.POST.get('description')
        new_item = Item(id=item_id, name=item_name, brand=item_brand, count=item_count, description=item_description)
        new_item.save()
        return redirect('/items')
    return render(request, 'add_item.html')


@csrf_exempt
def remove_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        el = Item.objects.filter(id=item_id).first()
        if el is None:
            pass
        else:
            el.delete()
    context = {}
    result = []
    queryset = Item.objects.all()
    for el in queryset:
        answer = {'id': el.id, 'name': el.name, 'brand': el.brand, 'count': el.count, 'description': el.description}
        result.append(answer)
    context['items'] = result
    return render(request, 'remove_item.html', context)