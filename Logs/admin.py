from django.contrib import admin
from django.db.models.functions import Lower
from .models import log


class logadmin(admin.ModelAdmin):
    list_display = ['id','type', 'time_stamp','date_created','user','is_started']

    def get_ordering(self, request):
        return [Lower('time_stamp')]  # sort case insensitive


admin.site.register(log, logadmin)



