from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User as AppUser, CrimeType, Location, Report
from django.contrib.auth.models import User as AuthUser, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin


admin.site.unregister(AuthUser)
admin.site.unregister(Group)


@admin.register(AuthUser)
class CustomAuthUserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class CustomGroupAdmin(BaseGroupAdmin, ModelAdmin):
    list_display = ('name',)

    def get_fieldsets(self, request, obj=None):
        return [(None, {'fields': ['name']})]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'permissions' in form.base_fields:
            del form.base_fields['permissions']
        return form



@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    list_display = ('id', 'username', 'age', 'phone_number', 'status', 'gender', 'address','photo')
    search_fields = ('name', 'phone_number', 'address','password')
    list_filter = ('gender', 'status')
    ordering = ('id',)


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('id', 'city', 'district', 'address', 'latitude', 'longitude')
    search_fields = ('city', 'district', 'address')
    list_filter = ('address',)


@admin.register(CrimeType)
class CrimeTypeAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('id', 'user', 'crime_type', 'location', 'date_reported', 'is_verified')
    list_filter = ('crime_type', 'is_verified', 'date_reported')
    search_fields = ('user__name', 'crime_type__name', 'location__city')
    date_hierarchy = 'date_reported'
    ordering = ('-date_reported',)
