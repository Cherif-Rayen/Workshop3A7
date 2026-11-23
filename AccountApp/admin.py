from django.contrib import admin
from.models import *
from AppointementApp.models import Appointement
# Register your models here.
admin.site.register(User)
#class AppointementStacked(admin.StackedInline):
class AppointementStacked(admin.TabularInline):

    model=Appointement
    extra=1
admin.site.register(Patient)
class DoctorPersoClass(admin.ModelAdmin):
    inlines=[AppointementStacked,]   
admin.site.register(Doctor,DoctorPersoClass)
admin.site.register(Speciality)

