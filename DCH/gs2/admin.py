from django.contrib import admin
from gs2.models import Group, Chat

# Register your models here.

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'time_stamp', 'group']
