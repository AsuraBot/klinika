from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from peoples.models import Client, Doctor, Operator, MainOperator, Director, DoctorMain


# class PeopleInline(admin.TabularInline):
#     model = People
#     readonly_fields = ['name', 'phone', 'adress', 'dob', 'discount']
#     exclude = ['user']
#     can_delete = False
#     max_num = 0


# class PeopleAdmin(admin.ModelAdmin):
#     list_display = ['name', 'link_to_user', 'people_main', 'phone', 'adress', 'dob']
#     readonly_fields = ['user']
#     fields = ['people_main', 'user', 'name', 'phone', 'adress', 'dob', 'discount']
#     list_filter = ['people_main']

#     def link_to_user(self, obj):
#         if obj.user:
#             link = reverse('admin:users_userprofile_change', args=[obj.user.id])
#             return format_html('<a href="%s">%s</a>' % (link, obj.user.username))
#     link_to_user.short_description = 'Профиль'

    
admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Operator)
admin.site.register(MainOperator)
admin.site.register(Director)
admin.site.register(DoctorMain)