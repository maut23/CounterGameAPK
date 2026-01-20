[app]

# (str) Title of your application
title = Counter Game

# (str) Package name (use lowercase, no spaces)
package.name = countergame

# (str) Package domain (can be fake if not published)
package.domain = org.example

# (str) Source code filename
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include
source.include_patterns = assets/*

# (str) Application version
version = 1.0

# (str) Requirements (Python modules + Kivy)
requirements = python3,kivy

# (str) Icon of the app
icon.filename = assets/icon.png

# (str) Supported orientation (portrait, landscape)
orientation = portrait

# (bool) Whether to fullscreen
fullscreen = 1

# (str) Presplash image (optional)
presplash.filename = assets/icon.png

# (str) Supported Android API
android.api = 33

# (str) Minimum API your app supports
android.minapi = 21

# (str) Android SDK build-tools version (stable)
android.build_tools_version = 33.0.2

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Python version to use
android.python_version = 3

# (list) Permissions your app may need
android.permissions = INTERNET

# (str) Extra Android arguments (optional)
# android.extra_gradle_dependencies =

[buildozer]

# (str) Log level
log_level = 2

# (str) Target platform
target = android

# (str) Whether to clean build before compiling
clean_build = True
android.sdk = 24
android.ndk = 23b
android.accept_sdk_license = True
