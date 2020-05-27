from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import *


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    plan = PlanSerializer()

    update_due_date = SerializerMethodField()

    class Meta:
        model = Student
        exclude = ("id", "created_at", "updated_at", "due_date")

    def set_update_due_date(self, object):
        if object.due_date is None:
            date = object.application_date
        else:
            date = object.due_date

        object.due_date = object.due_date.replace(month=date.month+1)

        return date

    def get_update_due_date(self, object):
        return object.due_date




class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'