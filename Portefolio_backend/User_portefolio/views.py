from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact, TypeDeProjet, Language, Competence, CategorieCompetence, NiveauCompetence
)

from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    LocalisationSerializer, ServiceSerializer, ReseauSocialSerializer,
    PriseDeContactSerializer, LanguageSerializer, CompetenceSerializer
)

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ProjetViewSet(ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["type_de_projet"]

    @action(detail=False, methods=["get"], url_path="types")
    def types(self, request):
        """Retourne la liste des types de projet disponibles (clé + libellé)."""
        types = [{"key": tag.name, "label": tag.value} for tag in TypeDeProjet]
        return Response(types)


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

    def perform_create(self, serializer):
        """Envoie un email de confirmation après la création d'un contact"""
        contact = serializer.save()
        
        # Vérifier si la configuration email est disponible
        email_configured = (
            settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend' or
            (hasattr(settings, 'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER)
        )
        
        if not email_configured:
            print("⚠️ Configuration email non disponible - Email non envoyé")
            return
        
        # Préparer le contenu de l'email de confirmation
        sujet = "Confirmation de réception de votre message"
        message = f"""Bonjour {contact.nom_complet},

Nous avons bien reçu votre message concernant : {contact.objet}

Voici un récapitulatif de votre demande :
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Objet : {contact.objet}
Message : {contact.message}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nous reviendrons vers vous dans les plus brefs délais.

Cordialement,
L'équipe Portfolio
        """
        
        try:
            # Envoyer l'email de confirmation à l'utilisateur
            send_mail(
                subject=sujet,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=True,  # Ne pas bloquer si l'envoi échoue
            )
            print(f"✅ Email de confirmation envoyé à {contact.email}")
        except Exception as e:
            # En cas d'erreur d'envoi, on log mais on ne bloque pas la création
            print(f"❌ Erreur lors de l'envoi de l'email : {e}")
            # L'enregistrement du contact reste valide même si l'email échoue


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CompetenceViewSet(ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categorie", "niveau"]

    @action(detail=False, methods=["get"], url_path="categories")
    def categories(self, request):
        """Retourne la liste des catégories de compétences disponibles."""
        categories = [{"key": tag.name, "label": tag.value} for tag in CategorieCompetence]
        return Response(categories)

    @action(detail=False, methods=["get"], url_path="niveaux")
    def niveaux(self, request):
        """Retourne la liste des niveaux de compétences disponibles."""
        niveaux = [{"key": tag.name, "label": tag.value} for tag in NiveauCompetence]
        return Response(niveaux)
