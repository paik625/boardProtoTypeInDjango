from django.contrib import admin
from .models import *


class BOARDAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content', 'create_at', 'hit' ]

admin.site.register(BOARD, BOARDAdmin)