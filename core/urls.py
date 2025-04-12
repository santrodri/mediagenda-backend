from django.urls import (path, include)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views

from avatar.urls import urlpatterns as avatar_urls
from user.urls import  urlspatterns as user_urls

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # essas implementações vão ser feitas manualmente
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/view_token/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/blacklist', jwt_views.TokenBlacklistView.as_view(), name='blacklist'),
    path('api/avatar/', include(avatar_urls)),
    path('api/', include(user_urls)),
]
