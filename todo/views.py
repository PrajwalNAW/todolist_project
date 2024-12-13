from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
