from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(DocLogin)
admin.site.register(DocDetails)
admin.site.register(Patients)
admin.site.register(Sign)
admin.site.register(Comments)