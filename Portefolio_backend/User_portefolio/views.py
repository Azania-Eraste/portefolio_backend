from rest_framework.viewsets import ModelViewSet
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact
)

from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    LocalisationSerializer, ServiceSerializer, ReseauSocialSerializer,
    PriseDeContactSerializer
)

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ProjetViewSet(ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class LocalisationViewSet(ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ReseauSocialViewSet(ModelViewSet):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer


class PriseDeContactViewSet(ModelViewSet):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
