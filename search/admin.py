from django.contrib import admin
from .models import Data
from django.db import models
from django.forms import Textarea
# Register your models here.

# @admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': Textarea(
                       attrs={'rows': 3,
                              'cols': 30})},
    }
    list_display = ('ent_seq','keb','reb','trans_det','tieng_viet')
    # list_display = ('keb','ent_seq','reb','trans_det')
    list_editable = ('keb','reb','trans_det','tieng_viet')
    list_per_page = 9
admin.site.register(Data,DataAdmin)