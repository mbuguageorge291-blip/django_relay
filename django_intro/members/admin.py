from django.contrib import admin
from .models import Members
# Register your models here.

class MembersAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'joined_date')
    search_fields = ('firstname', 'lastname')
admin.site.register(Members, MembersAdmin)
