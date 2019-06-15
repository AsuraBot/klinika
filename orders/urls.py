from django.urls import path
from orders import views

urlpatterns = [
    path('booknow/', views.booknow, name='booknow'),
    path('doctorbooknow/', views.doctorbooknow, name='doctorbooknow'),
    path('servicefilter/', views.servicefilter, name='servicefilter'),
    path('doctorfilter/', views.doctorfilter, name='doctorfilter'),
    path('cityfilter/', views.cityfilter, name='cityfilter'),
    path('datetimefilter/', views.datetimefilter, name='datetimefilter'),
    path('ordercreate/', views.ordercreate, name='ordercreate'),
    path('doctorschedulebooknow/', views.doctorschedulebooknow, name='doctorschedulebooknow'),
    path('scheduleorder/', views.ScheduleOrderView.as_view(), name='scheduleorder'),
]