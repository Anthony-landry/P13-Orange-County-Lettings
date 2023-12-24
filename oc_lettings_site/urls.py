from django.contrib import admin
from django.urls import path, include

from . import views
from .views import error500

handler404 = "oc_lettings_site.views.error404"
handler500 = "oc_lettings_site.views.error500"


def trigger_error(request):
    print(1 / 0)


urlpatterns = [
    path('', views.index, name='index'),
    path("error-500", error500, name="error-500"),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)

]
