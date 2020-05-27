from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from .serializers import *
from rest_framework import filters


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['name', 'cpf']
    lookup_field = 'name'

    queryset = Student.objects.filter(active=True)


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    queryset = Payment.objects.all()[:10]


class ExerciseViewSet(ModelViewSet):

    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Exercise.objects.all()[:10]
    serializer_class = ExerciseSerializer


class WorkoutViewSet(ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Workout.objects.all()[:10]
    serializer_class = WorkoutSerializer


class PlanViewSet(ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Plan.objects.all()[:10]
    serializer_class = PlanSerializer
