from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  views.UserList.as_view(), name="user_list"),
    
    url(r'^(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name="user_details"),
    url(r'^(?P<user_id>[0-9]+)/payments$',views.PaymentHistoryOfUser.as_view(),name="user_payment_history"),
    
]