from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['title']
    list_filter = ['price']
    search_fields = ['title', 'price']

admin.site.register(Course, CourseAdmin)
