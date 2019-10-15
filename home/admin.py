from django.contrib import admin
from .models import Subject, HomePage, Member, Projects, Services, UploadedWork

# Register your models here.
admin.site.register(Subject)
admin.site.register(HomePage)
admin.site.register(Member)
admin.site.register(Projects)
admin.site.register(Services)
admin.site.register(UploadedWork)