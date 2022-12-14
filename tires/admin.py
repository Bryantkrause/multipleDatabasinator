from django.contrib import admin

from .models import Tire, Activity, Location


admin.site.register(Activity)
admin.site.register(Location)
admin.site.register(Tire)