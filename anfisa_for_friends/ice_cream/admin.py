from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'price'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'price'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


# # Этот вариант сработает для всех моделей приложения.
# # Вместо пустого значения в админке будет отображена строка "Не задано".
# admin.site.empty_value_display = 'Не задано'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
