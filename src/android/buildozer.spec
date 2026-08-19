[app]

# --- Infos de base ---
title = Neon Run
package.name = neonrun
package.domain = org.isax820

# Dossier contenant main.py
source.dir = .

source.include_exts = py,png,jpg,jpeg,ttf,ogg,wav

version = 2026.7.27

# VersionCode Android
android.numeric_version = 1


# --- Dependances Python ---
requirements = python3==3.10.14,hostpython3==3.10.14,pygame


# --- Orientation / affichage ---
orientation = landscape
fullscreen = 1


# --- Icone et image de lancement ---
icon.filename = %(source.dir)s/../../assets/icon_android.png
presplash.filename = %(source.dir)s/../../assets/icon_android.png

android.presplash_color = #0A0A0F


# --- Permissions Android ---
android.permissions =


# --- SDK Android ---
android.accept_sdk_license = True


# --- Config Android ---
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Générer un Android App Bundle (.aab) pour Google Play
android.release_artifact = aab

android.orientation = landscape


[buildozer]

log_level = 2
