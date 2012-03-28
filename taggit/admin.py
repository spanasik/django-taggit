from django.contrib import admin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        TaggedItemInline
    ]
    list_display = ('name', 'slug')


admin.site.register(Tag, TagAdmin)
