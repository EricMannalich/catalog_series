from rest_framework.routers import DefaultRouter

from apps.principal.api.api import *

router = DefaultRouter()
router.register(r'genero',GeneroViewSet, basename = 'genero')
router.register(r'color',ColorViewSet, basename = 'color')
router.register(r'serie',SerieViewSet, basename = 'serie')
router.register(r'episodio',EpisodioViewSet, basename = 'episodio')
router.register(r'puntuacion',PuntuacionViewSet, basename = 'puntuacion')
urlpatterns = router.urls