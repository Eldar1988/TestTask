from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image, ImageAction


admin.site.register(ImageAction)


@admin.register(Image)
class ImageUploaderAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'user', 'image', 'date']
    list_filter = ['date', 'user']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} style="height: 50px; width: 50px; object-fit: contain;">')

    get_image.short_description = 'Миниатюра'



