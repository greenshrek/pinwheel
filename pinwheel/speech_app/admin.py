from django.contrib import admin
from speech_app.models import AcccessRecord, Topic, Webpage

# Register your models here.
admin.site.register(AcccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)