# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView
# from django.conf import settings
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     client_class = OAuth2Client
#     callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL

from rest_framework import generics, permissions
from django.contrib.auth import login

from .serializers import SignupSerializer

class SignUp(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
        login(self.request, serializer.instance, backend="django.contrib.auth.backends.ModelBackend")