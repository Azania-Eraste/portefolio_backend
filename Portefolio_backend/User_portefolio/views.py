import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact, TypeDeProjet,
    Language, Competence, CategorieCompetence, NiveauCompetence
)
from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    LocalisationSerializer, ServiceSerializer, ReseauSocialSerializer,
    PriseDeContactSerializer, LanguageSerializer, CompetenceSerializer
)
from .permissions import IsAdminOrReadOnly, IsAdminOrCreateOnly

logger = logging.getLogger(__name__)


class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjetViewSet(ModelViewSet):
    queryset = Projet.objects.select_related('utilisateur').prefetch_related('languages', 'competences').all()
    serializer_class = ProjetSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type_de_projet"]

    @action(detail=False, methods=["get"], url_path="types")
    def types(self, request):
        """Retourne la liste des types de projet disponibles."""
        types = [{"key": tag.name, "label": tag.value} for tag in TypeDeProjet]
        return Response(types)


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.prefetch_related('services', 'services__localisation').all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminOrReadOnly]


class LocalisationViewSet(ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.select_related('experience', 'localisation').all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReseauSocialViewSet(ModelViewSet):
    queryset = ReseauSocial.objects.select_related('utilisateur').all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [IsAdminOrReadOnly]


class PriseDeContactViewSet(ModelViewSet):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [IsAdminOrCreateOnly]

    def perform_create(self, serializer):
        """Envoie un email de confirmation apres la creation d'un contact."""
        contact = serializer.save()

        email_configured = (
            settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend'
            or (hasattr(settings, 'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER)
        )

        if not email_configured:
            logger.warning("Configuration email non disponible - Email non envoye")
            return

        sujet = "Confirmation de reception de votre message"
        message = (
            f"Bonjour {contact.nom_complet},\n\n"
            f"Nous avons bien recu votre message concernant : {contact.objet}\n\n"
            f"Recap :\n"
            f"{'=' * 40}\n"
            f"Objet : {contact.objet}\n"
            f"Message : {contact.message}\n"
            f"{'=' * 40}\n\n"
            f"Nous reviendrons vers vous dans les plus brefs delais.\n\n"
            f"Cordialement,\n"
            f"L'equipe Portfolio"
        )

        try:
            send_mail(
                subject=sujet,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=True,
            )
            logger.info("Email de confirmation envoye a %s", contact.email)
        except Exception as e:
            logger.error("Erreur lors de l'envoi de l'email : %s", e)


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminOrReadOnly]


class CompetenceViewSet(ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categorie", "niveau"]

    @action(detail=False, methods=["get"], url_path="categories")
    def categories(self, request):
        """Retourne la liste des categories de competences disponibles."""
        categories = [{"key": tag.name, "label": tag.value} for tag in CategorieCompetence]
        return Response(categories)

    @action(detail=False, methods=["get"], url_path="niveaux")
    def niveaux(self, request):
        """Retourne la liste des niveaux de competences disponibles."""
        niveaux = [{"key": tag.name, "label": tag.value} for tag in NiveauCompetence]
        return Response(niveaux)
