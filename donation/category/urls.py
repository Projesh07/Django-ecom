from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from category import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  views.CategoryList.as_view(), name="category_list"),
    url(r'^(?P<pk>[0-9]+)/$',views.CategoryDetail.as_view(),name="detail_category"),
    

]

#urlpatterns = format_suffix_patterns(urlpatterns)

# url(r'^create_user/$',  UserCreate.as_view(),name="create_user"),
# 	url(r'^update_user/(?P<id>[0-9]+)/$',  UserUpdate.as_view(),name="update_user"),
# 	url(r'^delete_user/(?P<id>[0-9]+)/$',  UserDelete.as_view(),name="delete_user"),
