from django.contrib import admin
from schedules.models import WorkTime, WorkDate

# Register your models here.


class WorkDateAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'get_times' ,'workcity']

    def get_times(self, obj):
        worktimes = [worktime.time.strftime('%H:%M') for worktime in obj.worktimes.all()]
        if len(worktimes):
            return "; ".join(worktimes)
        else:
            return " "


admin.site.register(WorkTime)
admin.site.register(WorkDate, WorkDateAdmin)
# admin.site.register(WorkCity)