from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from campaign import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  views.CampaignList.as_view(), name="campaign_list"),
     # url(r'^(?P<campaign_id>[0-9]+)/$',views.CampaignDetail.as_view(), name="detail_campaign"),
    # url(r'^documents/$',views.DocumentList.as_view(),name="document_list"),
    # url(r'^comments/$',views.CommentsFromCampaign.as_view(),name="comment_list"),

    url(r'^tags/$',views.TagList.as_view(),name="tag_list"),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name="user_details"),
    url(r'^(?P<campaign_id>[0-9]+)/tags/$',views.TagListByCampaign.as_view(), name="tagList_by_campaign"),
    url(r'^(?P<campaign_id>[0-9]+)/documents/$',views.DocumentList.as_view(), name="documentList_by_campaign"),
    url(r'^(?P<campaign_id>[0-9]+)/comments/$',views.CommentsFromCampaign.as_view(), name="commentList_by_campaign"),
    url(r'^(?P<campaign_id>[0-9]+)/donates/$',views.DonateToCampaign.as_view(), name="donate_to_campaign"),

    url(r'^recent-donations/$',views.RecentDotanationsOfCampaign.as_view(),name="recent_donations"),
    url(r'^top-donations/$',views.TopDotanationsOfCampaign.as_view(),name="top_donations"),
    url(r'^(?P<slug>[\w-]+)/$', views.CampaignDetail.as_view(), name="detail_campaign"),

]

