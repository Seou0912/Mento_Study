from django.contrib import admin

from bookmark.models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link")


# Register your models here.
admin.site.register(Bookmark, BookmarkAdmin)
