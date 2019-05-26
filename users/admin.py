from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from users.models import UserProfile, MyGroup, Discount, DoctorMain

# Register your models here.


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'sur_name', 'adress', 'phone', 'email', 'dob')}),
        ('Для врачей', {'classes': ('collapse', ), 'fields': ('doctor_main', 'ref_doc', 'oklad', 'information', 'image' )}),
        ('Скидка', {'classes': ('collapse', ), 'fields': ('discount',)}),
        ('Агентство', {'classes': ('collapse', ), 'fields': ('agency',)}),
        (_('Permissions'), {'classes': ('collapse', ), 'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'classes': ('collapse', ), 'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserProfile, UserAdmin)
admin.site.unregister(Group)
admin.site.register(MyGroup)
admin.site.register(Discount)
admin.site.register(DoctorMain)