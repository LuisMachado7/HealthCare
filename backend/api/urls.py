# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, ClinicaViewSet

router = DefaultRouter()
router.register(r'clinicas', ClinicaViewSet)
router.register(r'medicos', MedicoViewSet)

urlpatterns = router.urls
