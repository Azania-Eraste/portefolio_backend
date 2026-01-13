from rest_framework.routers import DefaultRouter
from .views import (
    UtilisateurViewSet, ProjetViewSet, ExperienceViewSet,
    LocalisationViewSet, ServiceViewSet, ReseauSocialViewSet,
    PriseDeContactViewSet
)

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
router.register(r'projets', ProjetViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'localisations', LocalisationViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'reseaux', ReseauSocialViewSet)
router.register(r'contacts', PriseDeContactViewSet)

urlpatterns = router.urls
