from django.contrib import admin
from mysecoapp.models import Student

# Register your models here.
class SudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']
admin.site.register(Student,SudentAdmin)
