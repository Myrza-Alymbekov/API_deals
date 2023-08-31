from django.db import transaction
from django.db.models import Sum

from .models import Customer, Gem, Deal


@transaction.atomic
def read_and_save_deals(file):
    """
    Функция для получения информации о совершенных сделках с csv-файла
    и записи в БД.

    В случае, если на каком-то этапе выполнения функции произойдет ошибка,
    все объекты вернутся к исходному (до выполнения функции) состоянию.

    """
    deal_list = []
    for line in file.readlines():
        row = line.decode('utf-8').strip()
        customer, item, total, quantity, date = row.split(',')
        if customer == 'customer' and item == 'item' and total == 'total':
            continue
        customer, _ = Customer.objects.get_or_create(username=customer)
        gem, _ = Gem.objects.get_or_create(name=item)
        deal_list.append(Deal(customer=customer,
                              gem=gem,
                              total=total,
                              quantity=quantity,
                              date=date))
    Deal.objects.bulk_create(deal_list)


def get_info_about_top_customers():
    """
        Функция для получения информации о 5 клиентах,
        потративших наибольшую сумму за весь период.
        """
    top_customers = Customer.objects.annotate(
        spent_money=Sum('deal__total')
    ).order_by('-spent_money')[:5]

    gems_bought_by_top_customers = Gem.objects.filter(
        deal__customer__in=top_customers
    ).distinct()

    response_data = []
    for customer in top_customers:
        other_top_customers = Customer.objects.filter(
            id__in=[cust.id for cust in top_customers if cust != customer])
        gems_bought = list(
            gems_bought_by_top_customers.filter(deal__customer=customer)
            .filter(deal__customer__in=other_top_customers)
            .values_list('name', flat=True)
        )
        response_data.append({
            'username': customer.username,
            'spent_money': customer.spent_money,
            'gems': gems_bought
        })
    return response_data
