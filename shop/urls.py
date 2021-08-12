from django.apps import apps
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from django.views.i18n import JavaScriptCatalog
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from channels.http import AsgiHandler
from channels.routing import URLRouter
from django.urls import path, re_path

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
admin.autodiscover()

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
]


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)