from ariadne.asgi import GraphQL
from channels.http import AsgiHandler
from channels.routing import URLRouter
from cms.sitemaps import CMSSitemap
from django.apps import apps
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
from ariadne.contrib.django.views import GraphQLView
from rest_framework import routers, serializers, viewsets
from flatblocks.views import edit
from django.contrib.auth.decorators import login_required
from .schema import schema
import debug_toolbar

admin.autodiscover()

schema = ...

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('', include(apps.get_app_config('oscar').urls[0])),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path("api/", include("oscarapi.urls")),
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r"^badges/", include("pinax.badges.urls", namespace="pinax_badges")),
    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    path('api-auth/', include('rest_framework.urls')),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
    url(r'^flatblocks/(?P<pk>\d+)/edit/$', login_required(edit),
        name='flatblocks-edit'),
    path('__debug__/', include(debug_toolbar.urls)),
    url(r'^keycloak/', include('django_keycloak.urls')),
]

application = URLRouter([
    path("graphql/", GraphQL(schema, debug=True)),
    re_path(r"", AsgiHandler),
])


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)