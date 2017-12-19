# facebook authentication
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.serializers import SocialLoginSerializer

class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter
	client_class = OAuth2Client
	callback_url = 'http://localhost:8000/rest_auth/facebook'

	# serializer_class = SocialLoginSerializer

	# def process_login(self):
	# 	get_adapter(self.request).login(self.request, self.user)

# google authentication
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

# from rest_auth.social_serializers import TwitterLoginSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/rest_auth/google'



# twitter authentication
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.views import LoginView
from rest_auth.social_serializers import TwitterLoginSerializer

class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

