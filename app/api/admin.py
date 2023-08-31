from django.contrib import admin
from .models import Customer, Gem, Deal


admin.site.register(Gem)
admin.site.register(Customer)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('customer', 'gem', 'total', 'quantity', 'date')
    search_fields = ('gem__name', 'customer__username')
