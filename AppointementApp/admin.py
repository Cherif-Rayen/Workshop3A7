from django.contrib import admin
from.models import Appointement
from AccountApp.models import Doctor
# Register your models here.
@admin.action(description="make them confirmed")
def confirmed_appointement(model,request,queryset):
    queryset.update(status="CONFIRMED")
#admin.site.register(Appointement)
class DoctorPerso(admin.StackedInline):
    model = Doctor
@admin.register(Appointement)
class AppointementAdminPers(admin.ModelAdmin):
    #inline = [DoctorPerso, ]
    actions= [confirmed_appointement]
    list_display =('reason','status','duration_minutes','appointement_date','created_at', 'update_at')
    list_filter =('status','appointement_date')
    list_editable=('status',)
    search_fields=('status','reason',)
    list_per_page =2
    ordering=('appointement_date',)
    fieldsets = (
       ('Description', {
        'fields': ('reason', 'prescription', 'status',)}),
       ('Date + duration ', {
          'fields': ('appointement_date', 'duration_minutes')
          }),
       ('Patients/Doctors', {
          'fields': ( 'patient','doctor')
          }),
        ('Planification', {
          'fields': ('created_at', 'update_at')
          }),
    )
    readonly_fields=('created_at', 'update_at')