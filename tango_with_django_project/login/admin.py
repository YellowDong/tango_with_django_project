from django.contrib import admin

from login.models import User, Confirm

admin.site.register(Confirm)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'has_confrimed')


admin.site.register(User, UserAdmin)