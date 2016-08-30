"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, handler400, handler403, handler404, handler500
from django.contrib import admin
# import django.views.defaults
from landing import views as landing_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', landing_views.index, name="landing_views_index"),
    url(r'^event/(?P<event_id>\d*)/$', landing_views.event, name="landing_views_index"),
    url(r'^thank_you/$', landing_views.thank_you, name="landing_views_thank_you"),
    url(r'^404/$', landing_views.handler404, ),
    url(r'^500/$', landing_views.handler500, ),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'landing.views.handler404'
handler500 = 'landing.views.handler500'

# urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                                 'document_root': settings.MEDIA_ROOT}))
