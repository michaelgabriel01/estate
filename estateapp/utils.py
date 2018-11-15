from functools import reduce

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginate(request, queryset, limit):
    paginator = Paginator(queryset, limit)
    page_number = request.GET.get('page')

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def search_by(request, queryset, fields):
    search = request.GET.get('s', '').strip()
    conditions = []

    if search and len(search) >= 2:
        for field_name in fields:
            kwarg = {'{}__icontains'.format(field_name): search}
            conditions.append(Q(**kwarg))

        query = conditions.pop()

        for condition in conditions:
            query |= condition

        return queryset.filter(query)

    return queryset
