from django.contrib import admin
from .models import OrganizationalMember


class OrganizationalMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'position', 'email', 'supervisor_display', 'phone_number')  # Отображаем ключевые поля
    search_fields = ('name', 'surname', 'position', 'email', 'phone_number')  # Поля для поиска
    list_filter = ('position',)  # Фильтры по должностям
    ordering = ('surname', 'name')  # Сортировка по фамилии и имени
    autocomplete_fields = ('supervisor',)  # Упрощённый выбор руководителя
    list_per_page = 20  # Количество записей на одной странице

    def supervisor_display(self, obj):
        """Показывает имя и фамилию руководителя"""
        if obj.supervisor:
            return f"{obj.supervisor.name} {obj.supervisor.surname}"
        return "Нет"
    supervisor_display.short_description = 'Руководитель'

# Регистрация модели в админке
admin.site.register(OrganizationalMember, OrganizationalMemberAdmin)
