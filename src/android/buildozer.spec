[app]

# --- Infos de base ---
title = Neon Run
package.name = neonrun
package.domain = org.isax820

# Dossier contenant main.py (le code adapte avec les controles tactiles)
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,ogg,wav

version = 2026.7.26

# Empeche le calcul automatique (parfois casse) du versionCode Android
# a partir de la version ci-dessus -> on le fixe nous-memes.
android.numeric_version = 1

# --- Dependances Python ---
# pas besoin de pypresence ici : le RPC Discord est deja rendu
# optionnel dans le code (try/except), donc on ne l'installe meme
# pas pour Android.
# pygame utilise un en-tete interne de CPython (longintrepr.h)
# supprime depuis Python 3.11 -> on force la compilation avec
# Python 3.10, qui a encore cet en-tete.
# hostpython3 doit obligatoirement avoir la meme version que python3.
requirements = python3==3.10.14,hostpython3==3.10.14,pygame

# --- Orientation / affichage ---
# Le jeu est concu en 900x600, plus large que haut -> paysage
orientation = landscape
fullscreen = 1

# --- Icone et image de lancement ---
# assets/ est a la racine du repo, alors que ce buildozer.spec vit
# dans src/android -> on remonte de deux niveaux.
icon.filename = %(source.dir)s/../../assets/icon_android.png
presplash.filename = %(source.dir)s/../../assets/icon_android.png
# Couleur de fond derriere le presplash pendant le chargement
android.presplash_color = #0A0A0F

# --- Permissions Android ---
# Neon Run ne fait ni reseau ni stockage externe, donc aucune
# permission particuliere n'est necessaire pour l'instant.
android.permissions =

# Accepte automatiquement les licences du SDK Android.
# Indispensable en CI (GitHub Actions) : sans ca, le build reste
# bloque en attendant une confirmation manuelle qui ne viendra jamais.
android.accept_sdk_license = True

# --- Config Android ---
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Empeche l'app de se fermer si le telephone tourne l'ecran
# (puisqu'on force le paysage de toute facon)
android.orientation = landscape

[buildozer]
log_level = 2
