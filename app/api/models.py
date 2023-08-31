from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя покупателя')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.username


class Gem(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Камень'
        verbose_name_plural = 'Камни'

    def __str__(self):
        return self.name


class Deal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE, verbose_name='Камень')
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Сумма сделки')
    quantity = models.IntegerField(verbose_name='Количество камней')
    date = models.DateTimeField(verbose_name='Дата и время сделки')

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return f'{self.customer} - {self.gem} - {self.total}'
