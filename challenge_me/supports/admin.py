from django.contrib import admin

from models import Support


class SupportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Support, SupportAdmin)
