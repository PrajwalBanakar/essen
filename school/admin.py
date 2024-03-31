from django.contrib import admin
from .models import StudentExtra,Notice,EventRegistration
# Register your models here.
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)


class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class EventRegistrationAdmin(admin.ModelAdmin):
    pass
admin.site.register(EventRegistration, EventRegistrationAdmin)


