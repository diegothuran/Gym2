from django.contrib import admin
from core import models


class StudentAdmin(admin.ModelAdmin):
    model = models.Student
    list_display = ['name']
    search_fields = ['name']


class PlanAdmin(admin.ModelAdmin):
    model = models.Plan
    list_display = ['name', 'value']
    search_fields = ['name']


class PaymentAdmin(admin.ModelAdmin):
    model = models.Payment
    list_display = ['get_student_name', 'created_at']
    search_fields = ['student__name']
    
    def get_student_name(self, obj):
        return obj.student.name

class ExerciseAdmin(admin.ModelAdmin):
    model = models.Exercise
    list_display = ['name']
    search_fields = ['name']


class WorkoutAdmin(admin.ModelAdmin):
    model = models.Workout
    list_display = ['name']

admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Exercise, ExerciseAdmin)
admin.site.register(models.Workout, WorkoutAdmin)
