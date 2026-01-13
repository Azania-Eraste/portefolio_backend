from django.contrib import admin
from .models import (
    Utilisateur, Projet, Experience, Localisation,
    Service, ReseauSocial, PriseDeContact
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
    list_display = ("titre", "utilisateur", "lien")
    list_filter = ("utilisateur",)
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
