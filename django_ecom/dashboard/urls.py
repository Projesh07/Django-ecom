from django.conf.urls import url
from .views.dashboard_view import DashboardView
from .views.login_view import LoginView  
from .views.login_view import LogoutView 
from .views.admin_view import  (AdminCreate, AdminUpdate, 
	AdminDelete,AdminGroupList,UserCreate,UserUpdate,UserDelete,
	UserList

	)
from django.conf.urls.static import static
from django.conf import settings
from category.views.category_view import CategoryList,CategoryCreate,CategoryUpdate,CategoryDelete

from django.contrib.auth.decorators import login_required
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  LoginView.as_view()),
    url(r'^logout/$',  LogoutView.as_view(),name="logout"),
    url(r'^dashboard/$',login_required(DashboardView.as_view()),name="dashboard"),
    url(r'^create/$',  AdminCreate.as_view(),name="create_group"),
    url(r'^list_group/$',  AdminGroupList.as_view(),name="list_group"),
    url(r'^list_user/$',  UserList.as_view(),name="list_user"),
    url(r'^create_user/$',  UserCreate.as_view(),name="create_user"),
	url(r'^update_user/(?P<id>[0-9]+)/$',  UserUpdate.as_view(),name="update_user"),
	url(r'^delete_user/(?P<id>[0-9]+)/$',  UserDelete.as_view(),name="delete_user"),
    # url(r'^list_category/$',  CategoryList.as_view(),name="list_category"),
    # url(r'^create_category/$',  CategoryCreate.as_view(),name="create_category"),
    # url(r'^update_category/(?P<id>[0-9]+)/$',  CategoryUpdate.as_view(),name="update_category"),
    # url(r'^delete_category/(?P<id>[0-9]+)/$', CategoryDelete.as_view(),name="delete_category"),
    
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)