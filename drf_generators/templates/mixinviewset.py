
__all__ = ['MIXIN_URL', 'MIXIN_VIEW']


MIXIN_URL = """from rest_framework.routers import SimpleRouter
from {{ app }} import views


router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


MIXIN_VIEW = """from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import {{ serializers|join:', ' }}
from .models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}ViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
{% endfor %}"""
