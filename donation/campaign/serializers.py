from rest_framework import serializers
from django.contrib.auth.models import User
from category.models import Category
from campaign.models import Campaign
from campaign.models import Documents
from campaign.models import Comments
from campaign.models import Donate
from campaign.models import Tag
# from campaign.models import CampaignsHasTags
# from campaign.serializers import CampaignHasTagsSerializer
class UserDetailsForDotanationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name','username','email')
        # fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','image','descriptions')

class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documents
        fields = ('id','content','content_type','campaign_id','url')

class CommentsFromCampaignSerializer(serializers.ModelSerializer):
    user        = UserDetailsForDotanationsSerializer();
    class Meta:
        model = Comments
        # fields = ('id','comments','campaign','user')
        fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('id','comments','campaign','user')
        fields = '__all__'

class DonatesFromCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        # fields = ('id','comments','campaign','user')
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        # fields = ('name')
        fields = ('id','name')

class CampaignSerializer(serializers.ModelSerializer):
    
    category    = CategorySerializer()   
    documents   = DocumentSerializer(many=True, read_only=True)
    tags        = TagSerializer(many=True, read_only=True)
    campaign_comment    = CommentsFromCampaignSerializer(many=True, read_only=True)
    campaign_donates    = DonatesFromCampaignSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ('id','title', 'story','amount','start_date','end_date','status','publish_date','category','documents','campaign_donates','total_donate','tags','campaign_comment',)
        # lookup_field = 'slug'
        # fields = '__all__'

class CampaignListSerializer(serializers.ModelSerializer):
    
    category    = CategorySerializer()   
    
    class Meta:
        model = Campaign
        fields = ('id','title','slug', 'story','amount','start_date','end_date','status','publish_date','category',)
        # fields = '__all__'


class CampaignByCategorySerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    
    class Meta:
        model = Campaign
        fields = ('title', 'story','amount','start_date','end_date','category')
        # fields = '__all__'




class TagListByCampaignSerializer(serializers.ModelSerializer):
    
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Campaign
        fields = ('id','tags')
        # fields = '__all__'

class CampaignInfoForDonationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campaign
        fields = ('id','title', 'story')
        # fields = '__all__'




class TopOrRecentDonationsSerializer(serializers.ModelSerializer):
    
    campaign    = CampaignInfoForDonationsSerializer();
    user        = UserDetailsForDotanationsSerializer();

    class Meta:
        model = Donate
        # fields = ('name')
        fields = ('id','amount','donate_at','campaign','user')

# data post request api call 

class DonateToCampaignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donate
        fields = ('id','campaign_id', 'amount', 'user_id')

