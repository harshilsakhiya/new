from django.contrib import admin

from .models import register,Deposit,Draw,Win

admin.site.register(register)
admin.site.register(Deposit)
admin.site.register(Draw)
admin.site.register(Win)
