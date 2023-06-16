from django.urls import path

from catalog.views import head, contacts

urlpatterns = [
     path("", contacts)
 ]

