from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html
from peoples.models import Client, Doctor, Operator, MainOperator, Director, DoctorMain, OutsideDoctor, Agent
from schedules.models import WorkDate


class WorkDateInline(admin.TabularInline):
    model = WorkDate
    extra = 0


class DoctorAdmin(admin.ModelAdmin):
    inlines = [WorkDateInline]

    
admin.site.register(Client)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(OutsideDoctor)
admin.site.register(Agent)
admin.site.register(Operator)
admin.site.register(MainOperator)
admin.site.register(Director)
admin.site.register(DoctorMain)
admin.site.unregister(Group)