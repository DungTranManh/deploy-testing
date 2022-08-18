from django.contrib import admin
from .models import Data
# Register your models here.

# @admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('ent_seq','keb','reb','trans_det','tieng_viet')
    # list_display = ('keb','ent_seq','reb','trans_det')
    list_editable = ('keb','reb','trans_det','tieng_viet')
    list_per_page = 8
admin.site.register(Data,DataAdmin)