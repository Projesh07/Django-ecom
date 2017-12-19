from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings
from category.views.category_view import (CategoryList,CategoryCreate,
	CategoryUpdate,CategoryDelete)

from category.views.menu_view import (
	MenuCreate,MenuList,MenuUpdate,MenuDelete)

from category.views.product_view import (
    ProductCreate,ProductList,ProductUpdate,ProductDelete)   

from category.views.featured_product_view import (
    FeaturedProductCreate,FeaturedProductList,FeaturedProductUpdate,FeaturedProductDelete)  

from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^list_category/$',  CategoryList.as_view(),name="list_category"),
    url(r'^create_category/$',  CategoryCreate.as_view(),name="create_category"),
    url(r'^update_category/(?P<id>[0-9]+)/$',  CategoryUpdate.as_view(),name="update_category"),
    url(r'^delete_category/(?P<id>[0-9]+)/$', CategoryDelete.as_view(),name="delete_category"),


    url(r'^list_menu/$',  MenuList.as_view(),name="list_menu"),
    url(r'^create_menu/$',  MenuCreate.as_view(),name="create_menu"),
    url(r'^update_menu/(?P<id>[0-9]+)/$',  MenuUpdate.as_view(),name="update_menu"),
    url(r'^delete_menu/(?P<id>[0-9]+)/$', MenuDelete.as_view(),name="delete_menu"),


    url(r'^list_product/$',  ProductList.as_view(),name="list_product"),
    url(r'^create_product/$',  ProductCreate.as_view(),name="create_product"),
    url(r'^update_product/(?P<id>[0-9]+)/$',  ProductUpdate.as_view(),name="update_product"),
    url(r'^delete_product/(?P<id>[0-9]+)/$', ProductDelete.as_view(),name="delete_product"),
    
    url(r'^list_featured_product/$',  FeaturedProductList.as_view(),name="list_featured_product"),
    url(r'^create_featured_product/$',  FeaturedProductCreate.as_view(),name="create_featured_product"),
    url(r'^update_featured_product/(?P<id>[0-9]+)/$',  FeaturedProductUpdate.as_view(),name="update_featured_product"),
    url(r'^delete_featured_product/(?P<id>[0-9]+)/$', FeaturedProductDelete.as_view(),name="delete_featured_product"),



        
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)