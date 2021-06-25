from django.contrib import admin

# Register your models here.
from .models import Fanpage

class FanpageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fanpage, FanpageAdmin)
