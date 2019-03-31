from django.contrib import admin
from orders.models import Order, ServiceInOrder, AnalysisInOrder

# Register your models here.

class ServiceInline(admin.TabularInline):
    model = ServiceInOrder
    extra = 0


class AnalysisInline(admin.TabularInline):
    model = AnalysisInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ServiceInline, AnalysisInline]


admin.site.register (Order, OrderAdmin)