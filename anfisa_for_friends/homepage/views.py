# Для применения Q-объектов их нужно импортировать:
from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream
from ice_cream.models import Category


def index(request):
    template_name = 'homepage/index.html'
    # Запрашиваем нужные поля из базы данных:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)


# Через прямые фильтры
# def index(request):
#     template = 'homepage/index.html'
#     # Запрос:
#     ice_cream_list = IceCream.objects.values(
#         'id', 'title', 'description'
#         # Верни только те объекты, у которых в поле is_on_main указано True:
#         ).filter(
#             is_on_main__exact=True, is_published=True  # Обьединили 2 условия,
#                                                        # аналог AND
#             )
# # Исключи те объекты, у которых is_published=False:
# # .exclude(is_published=False)
#     # Полученный из БД QuerySet передаём в словарь контекста:
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
#     return render(request, template, context)


# # Через Q модели
# def index(request):
#     template_name = 'homepage/index.html'
#     ice_cream_list = IceCream.objects.values(
#         'id', 'title', 'description'
#     ).filter(
#         # Делаем запрос, объединяя два условия
#         # через Q-объекты и оператор AND:
#         Q(is_published=True) & (Q(is_on_main=True)
#                                 | Q(title__contains='пломбир'))
#         # (Q(is_on_main=True) & Q(is_published=True))
#         # | (Q(title__contains='пломбир') & Q(is_published=True))
#     )
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)


# def index(request):
#     template_name = 'homepage/index.html'
#     categories = Category.objects.values(
#         'id', 'output_order', 'title'
#     ).order_by(
#         # Сортируем записи по значению поля output_order,
#         # а если значения output_order у каких-то записей равны -
#         # сортируем эти записи по названию в алфавитном порядке.
#         'output_order', 'title'
#     )
#     context = {
#         'categories': categories
#     }
#     return render(request, template_name, context)

# def index(request):
#     template_name = 'homepage/index.html'
#     ice_cream_list = IceCream.objects.values(
#         'id', 'title', 'description', 'wrapper__title'
#     ).filter(
#         is_published=True, is_on_main=True
#     ).order_by('title')[1:4]
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)

# # Получение из связанной таблицы:
# JOIN c помощью метода .values()
# def index(request):
#     template_name = 'homepage/index.html'
#     # ice_cream_list = IceCream.objects.all()
#     ice_cream_list = IceCream.objects.values(
#         'id', 'title', 'description', 'category__title'
#     ).filter(
#         category__is_published=True
#     )
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)


# # JOIN c помощью .select_related()
# def index(request):
#     template_name = 'homepage/index.html'
#     ice_cream_list = IceCream.objects.select_related(
#         'category'
#         ).filter(
#             category__is_published=True
#         )
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)
