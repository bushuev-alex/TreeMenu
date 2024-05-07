from django.contrib import admin
from menu.models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ["name"]
    list_display_links = ["name"]
    ordering = ["name"]


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuAdmin
    list_display = ["menu", "name", "url", "position", "parent"]
    list_display_links = ["name", "parent"]
    list_filter = ["menu", "name", "parent"]
    ordering = ["name"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
