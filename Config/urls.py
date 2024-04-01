from django.contrib import admin
from django.urls import path, include
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # drf-spectacular:
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # end drf-spectacular:
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
    path('shop/', include('shop.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
