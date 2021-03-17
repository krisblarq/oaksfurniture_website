from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Shop.urls')),
    path('account/', include('App_Login.urls')),
]
]


urlpatterns += staticfiles_urlpatterns()
urlspatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
