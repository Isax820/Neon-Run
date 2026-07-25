[app]

# --- Infos de base ---
title = Neon Run
package.name = neonrun
package.domain = org.isax820

# Dossier contenant main.py (le code adapté avec les controles tactiles)
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,ogg,wav

version = 1.0

# --- Dependances Python ---
# pas besoin de pypresence ici : le RPC Discord est deja
# rendu optionnel dans le code (try/except), donc on ne l'installe
# meme pas pour Android.
requirements = python3,pygame

# --- Orientation / affichage ---
# Le jeu est concu en 900x600, plus large que haut -> paysage
orientation = landscape
fullscreen = 1

# --- Icone et image de lancement (optionnel, a adapter si tu en as) ---
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# --- Permissions Android ---
# Neon Run ne fait ni reseau ni stockage externe, donc aucune
# permission particuliere n'est necessaire pour l'instant.
android.permissions =

# --- Config Android ---
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Empeche l'app de se fermer si le telephone tourne l'ecran
# (puisqu'on force le paysage de toute facon)
android.orientation = landscape

[buildozer]
log_level = 2
