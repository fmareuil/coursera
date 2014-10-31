from django.contrib import admin
from django import forms
from .models import Course, Teacher


# Register your models here.
class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course


class CourseAdmin(admin.ModelAdmin):
    # list_display = ('__unicode__', )
    # list_display = ('full_name', 'age' , 'profession')
    # list_filter = ('age', 'profession')
    form = CourseAdminForm


class TeacherAdminForm(forms.ModelForm):
    class Meta:
        model = Teacher


class TeacherAdmin(admin.ModelAdmin):
    # list_display = ('__unicode__', )
    # list_display = ('full_name', 'age' , 'profession')
    # list_filter = ('age', 'profession')
    form = TeacherAdminForm

admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)