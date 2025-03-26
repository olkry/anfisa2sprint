from django.shortcuts import render, get_object_or_404

from ice_cream.models import IceCream


# def ice_cream_detail(request, pkd):
#     template = 'ice_cream/detail.html'
#     '''
#     # # Вызываем .get() и в его параметрах указываем условия фильтрации:
#     ice_cream = IceCream.objects.get(pk=pkd)

#     # Отфильтруй объект модели IceCream,
#     # у которого pk равен значению переменной из пути.
#     # Если такого объекта не существует - верни 404 ошибку:
#     ice_cream = get_object_or_404(IceCream, pk=pkd)
#     # Это аналог записи:
    
#         try:
#         # Пытаемся получить объект с заданным pk:
#             ice_cream = IceCream.objects.get(pk=pk)
#         # Если объект не найден...
#         except IceCream.DoesNotExist:
#             # ...выбрасываем исключение Http404
#             raise Http404('Такого мороженого не существует.')
#             # Специальный обработчик перехватит выброшенное исключение
#             # и среагирует установленным образом; 
#             # по умолчанию -вернёт пользователю стандартную страницу ошибки404.
    
#     '''
#     ice_cream = get_object_or_404(
#         IceCream.objects.values('title', 'description'),
#         pk=pkd
#         )
#     context = {
#         'ice_cream': ice_cream,
#     }
#     return render(request, template, context)

def ice_cream_detail(request, pkd):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title', 'description'
            ).filter(is_published=True),
        pk=pkd
        )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
