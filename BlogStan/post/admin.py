from django.contrib import admin
from . import models

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.Comment
    
class AdminA(admin.ModelAdmin):
    inlines=[GroupMemberInline ]

admin.site.register(models.Post,AdminA)

