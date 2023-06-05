from rest_framework import routers
from core import viewsets

router = routers.DefaultRouter()
router.register(r'regras', viewsets.RegraViewSet)
router.register(r'acaodecorrecao', viewsets.AcaoDeCorrecaoViewSet)
router.register(r'correcaodedados', viewsets.ConjuntoDeDados, basename='conjunto_de_dados')
