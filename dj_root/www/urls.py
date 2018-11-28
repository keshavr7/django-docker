from django.conf.urls import include, url
from django.contrib import admin
import core.views

urlpatterns = [
    url(r'^', core.views.hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='accounts')),
]
