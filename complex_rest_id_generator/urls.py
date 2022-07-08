from django.urls import re_path
from .views.id_generator import IdGenerator


urlpatterns = [
    re_path(r'^generate-id/?$', IdGenerator.as_view())
]