from django.conf.urls import url, include
from rest_framework import routers
from api.services.user_services import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation ')
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', schema_view),
    url(r'api/pedidos-compra', UserServices.as_view()),
]