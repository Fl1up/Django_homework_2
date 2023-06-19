from django.conf import settings
from django.templatetags.static import static
from django.urls import path

from catalog.views import head

urlpatterns = [
     path("", head)
 ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)