from django.contrib import admin
from merged_inlines.admin import MergedInlineAdmin
from .models import Event, Section, Page, Text, Image


# Register your models here.

class TextInline(admin.TabularInline):
    model = Text
    extra = 0
    min_num = 0
    fields = ['order', 'text', 'imaget', 'imaget_tag']
    readonly_fields = ['imaget_tag']


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    min_num = 0
    fields = ['order', 'image', 'image_tag']
    readonly_fields = ['image_tag']



class SectionAdmin(MergedInlineAdmin):
    model = Section
    inlines = [
        ImageInline, TextInline
    ]
    merged_inline_order = 'order'

    
 
class PageAdmin(admin.ModelAdmin):
    model = Page
 
class EventAdmin(admin.ModelAdmin):
    exclude = ('active', 'published_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.site_header = "GluckGluck Admin"
admin.site.site_title = ""
admin.site.index_title = ""
