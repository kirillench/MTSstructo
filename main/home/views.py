from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import OrganizationalMember


def base(request):
    return render(request, 'base.html')


def search(request):
    query = request.GET.get('query', '')
    if query:
        # Фильтрация по всем ключевым полям
        employees = OrganizationalMember.objects.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(position__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
        )
    else:
        employees = OrganizationalMember.objects.all()  # Если нет запроса, показываем всех сотрудников
    return render(request, 'search.html', {'employees': employees, 'query': query})


def drevo(request):
    # Получаем всех сотрудников
    employees = OrganizationalMember.objects.all()
    # Формируем словарь иерархии
    def build_hierarchy(supervisor_id=None):
        nodes = employees.filter(supervisor_id=supervisor_id)
        return [
            {
                'employee': node,
                'children': build_hierarchy(node.id)
            }
            for node in nodes
        ]

    hierarchy = build_hierarchy()  # Создаём дерево
    return render(request, 'drevo.html', {'hierarchy': hierarchy})


