from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile
from campaign.models import Donate
from campaign.serializers import CampaignInfoForDonationsSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    # owner=serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ('id','image','provider','provider_id',)


class UserDetailsSerializer(serializers.ModelSerializer):

	profile=UserProfileSerializer()


	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','date_joined','profile',)
		# fields = '__all__'

class UsersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')


class PaymentHistoryOfUserSerializer(serializers.ModelSerializer):
    campaign    = CampaignInfoForDonationsSerializer();
    # user        = UserDetailsForDotanationsSerializer();

    class Meta:
        model = Donate
        # fields = ('name')
        fields = ('id','amount','donate_at','campaign',)

