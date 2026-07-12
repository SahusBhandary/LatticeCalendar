from rest_framework import generics, permissions
from django.contrib.auth import login

from .serializers import SignupSerializer

class SignUp(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
        login(self.request, serializer.instance, backend="django.contrib.auth.backends.ModelBackend")