from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Redirect root URL to Swagger UI
    path('', lambda request: redirect(reverse_lazy('docs'), permanent=True)),
    
    # Redirect /docs/ to /api/docs/
    path('docs/', lambda request: redirect(reverse_lazy('docs'), permanent=True)),
    
    # Django Admin
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include([
        path('', include('products.urls')),  # Products app
        path('', include('orders.urls')),  # Orders app
        path('', include('users.urls')),  # Users app
    ])),
    
    # API schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # API docs (Swagger UI)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += staticfiles_urlpatterns()