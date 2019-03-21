from django.contrib import admin
from analysis.models import Analysis, AnalysisType, Hospital

# Register your models here.

class HospitalInline(admin.TabularInline):
    model = Hospital
    extra = 0


class AnalysisAdmin(admin.ModelAdmin):
    inlines = [HospitalInline]
    list_display = ['name', 'type_of_analysis', 'is_active']
    list_editable = ['is_active']

class AnalysisTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']


# class HospitalAdmin(admin.ModelAdmin):
#     list_display = ['name', 'analysis', 'is_active']
#     list_editable = ['is_active']

    
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(AnalysisType,AnalysisTypeAdmin)
# admin.site.register(Hospital,HospitalAdmin)