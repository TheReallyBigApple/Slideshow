from django.contrib import admin

# Register your models here.
from ss_app.models import Photos


class PhotosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photos, PhotosAdmin)

