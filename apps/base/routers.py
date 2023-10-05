from rest_framework.routers import DefaultRouter

from apps.base.api import *

router = DefaultRouter()
router.register(r'menu',MenuViewSet, basename = 'menu')
router.register(r'filtro',FiltroViewSet, basename = 'filtro')
router.register(r'endbar',EndBarViewSet, basename = 'endbar')
urlpatterns = router.urls
