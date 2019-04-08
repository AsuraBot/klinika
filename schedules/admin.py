from django.contrib import admin
from schedules.models import WorkTime, WorkDate, WorkCity

# Register your models here.


class WorkDateAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'get_times' ,'workcity']

    def get_times(self, obj):
        worktimes = [worktime.time.strftime('%H:%M') for worktime in obj.worktimes.all()]
        return "%s - %s" % (worktimes[0], worktimes[-1])


admin.site.register (WorkTime)
admin.site.register (WorkDate, WorkDateAdmin)
admin.site.register (WorkCity)