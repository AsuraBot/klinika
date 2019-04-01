from django.contrib import admin
from schedules.models import WorkTime, WorkDate, WorkCity

# Register your models here.


admin.site.register (WorkTime)
admin.site.register (WorkDate)
admin.site.register (WorkCity)