from channels.http import AsgiHandler
from channels.routing import URLRouter
from cms.sitemaps import CMSSitemap
from django.apps import apps
import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib.auth.decorators import login_required
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.autodiscover()

def trigger_error(request):
    division_by_zero = 1 / 0


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sentry-debug/', trigger_error),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('', include(apps.get_app_config('oscar').urls[0])),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path("api/", include("oscarapi.urls")),
    url(r"^badges/", include("pinax.badges.urls", namespace="pinax_badges")),
    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    path('api-auth/', include('rest_framework.urls')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('payments/', include('payments.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include(tf_urls)),
    path('', include(tf_twilio_urls)),
    path('__debug__/', include(debug_toolbar.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comments/', include('django_comments_xtd.urls')),
]

application = URLRouter([
    re_path(r"", AsgiHandler),
])


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
admin.site.site_header = 'AlternateCMS' # Don't Remove
admin.site.site_title = 'AlternateCMS' # Don't Remove