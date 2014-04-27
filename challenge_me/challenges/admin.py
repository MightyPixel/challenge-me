from django.contrib import admin


from models import Challenge, ChallengeUpdate, ChallengeProof, ChallengeComment


class ChallengeAdmin(admin.ModelAdmin):
    pass

class ChallengeUpdateAdmin(admin.ModelAdmin):
    pass

class ChallengeProofAdmin(admin.ModelAdmin):
    pass

class ChallengeCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(ChallengeUpdate, ChallengeUpdateAdmin)
admin.site.register(ChallengeProof, ChallengeProofAdmin)
admin.site.register(ChallengeComment, ChallengeCommentAdmin)
