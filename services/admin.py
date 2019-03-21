from django.contrib import admin
from django.forms import ModelForm
from services.models import Service, ServiceMain
from users.models import UserProfile

# Register your models here.


class ServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args,**kwargs)
        self.fields['doctors'].queryset = UserProfile.objects.filter(groups=1)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service_main', 'price', 'is_active']
    list_display_links = ['name']
    list_editable = ['price','is_active']
    filter_horizontal = ['doctors']
    form = ServiceForm


class ServiceInline(admin.TabularInline):
    model = Service
    readonly_fields = ['name', 'price', 'doctors', 'ref_doc', 'ref_napr', 'ref_agent', 'is_active']
    can_delete = False
    max_num = 0


class ServiceMainAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceMain, ServiceMainAdmin)