from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
 
    # aother app from outside 
    # # Ckeditor
    # path('ckeditor/', include('ckeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # main apps
    path('', include('core.urls')),
    path('', include('books.urls')),
    path('', include('users.urls')),
    path('', include('carts.urls')),
    # path('', include('cart.urls')),
    path('', include('search.urls')),
    path('', include('wishlist.urls')),
    path('', include('order.urls')),
    path('', include('tools.urls')),
    path('', include('manage.urls')),
    
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
