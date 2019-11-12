from django.contrib import admin

# Register your models here.

from .models import Note

admin.site.register(Note)

class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note


