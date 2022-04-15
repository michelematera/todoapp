from rest_framework import generics, filters, permissions
from todoapp.applications.todo import models as todo_models
from . import serializers


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    queryset = todo_models.Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).filter(user=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = todo_models.Task.objects.all()
    lookup_field = 'id'

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).filter(user=self.request.user)


class UserCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserSerializer

