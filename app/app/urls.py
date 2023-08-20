from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from core.views import not_found_json_response, hello_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    ),
    path('api/', include('account.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('<path:unrecognized_path>/',
         not_found_json_response, name='unrecognized-path'),
    path('', hello_page, name='hello')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
