from django.contrib import admin
from .models import T1, T2, T3


@admin.register(T1)
class T1Admin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(T2)
class T2Admin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(T3)
class T3Admin(admin.ModelAdmin):
    list_display = ['name']
