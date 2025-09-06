from rest_framework import viewsets
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
