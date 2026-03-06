from django.contrib import admin
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Language, Competence, ReseauSocial, PriseDeContact
)
from django.contrib.auth.admin import UserAdmin


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = ("username", "email", "first_name", "last_name", "age", "telephone")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email", "first_name", "last_name", "telephone")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Informations supplémentaires", {
            "fields": (
                "photo_profil",
                "description",
                "age",
                "lien_cv",
                "telephone",
            )
        }),
    )


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("titre", "utilisateur", "lien", "type_de_projet")
    list_filter = ("utilisateur", "type_de_projet")
    search_fields = ("titre", "resume")
    autocomplete_fields = ("utilisateur",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "nom_entreprise", "date_debut", "date_fin")
    list_filter = ("nom_entreprise", "type_de_contrat")
    search_fields = ("role", "nom_entreprise")


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ("pays", "ville", "quartier")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("nom", "categorie", "niveau", "date_acquisition")
    list_filter = ("categorie", "niveau")
    search_fields = ("nom", "description")
    ordering = ("categorie", "nom")


@admin.register(ReseauSocial)
class ReseauSocialAdmin(admin.ModelAdmin):
    list_display = ("nom_plateforme", "utilisateur", "lien")
    list_filter = ("nom_plateforme",)
    search_fields = ("nom_plateforme", "lien")
    autocomplete_fields = ("utilisateur",)


@admin.register(PriseDeContact)
class PriseDeContactAdmin(admin.ModelAdmin):
    list_display = ("nom_complet", "email", "objet", "date_envoi")
    list_filter = ("date_envoi",)
    search_fields = ("nom_complet", "email", "objet", "message")
    readonly_fields = ("date_envoi",)
    ordering = ("-date_envoi",)
