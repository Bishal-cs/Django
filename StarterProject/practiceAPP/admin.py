from django.contrib import admin
from .models import all_typs_imgs, Image_review, specific_image, ImageProfile

# Inline for Image_review in all_typs_imgs admin
class ImageReviewInline(admin.TabularInline):
    model = Image_review
    extra = 2

# Admin for all_typs_imgs
class AllTypsImgsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_time_stamp')
    inlines = [ImageReviewInline]

# Admin for specific_image
class SpecificImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_info')
    filter_horizontal = ('image_type',)

# Admin for ImageProfile
class ImageProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_number', 'isshu_date', 'valid_until')

admin.site.register(all_typs_imgs, AllTypsImgsAdmin)
admin.site.register(specific_image, SpecificImageAdmin)
admin.site.register(ImageProfile, ImageProfileAdmin)