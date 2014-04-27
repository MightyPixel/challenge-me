from django.contrib import admin

from models import Cause, CauseComment


class CauseAdmin(admin.ModelAdmin):
    pass

class CauseCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cause, CauseAdmin)
admin.site.register(CauseComment, CauseCommentAdmin)
