from rest_framework import routers
from mainStart.viewsets import mainStartViewSet

router = routers.DefaultRouter()
router.register(r'mainStart', mainStartViewSet)