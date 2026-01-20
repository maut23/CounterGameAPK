[app]
# (change the title, package name as you like)
title = CounterGame
package.name = countergame
package.domain = org.maut23
source.dir = .
version = 0.1
orientation = portrait
fullscreen = 0

# Requirements
requirements = python3,kivy

# Android
android.sdk = 24
android.ndk = 25b
android.accept_sdk_license = True

# Permissions (optional, for Play Store)
android.permissions = INTERNET

# Target API (Play Store now needs 33+)
android.api = 33
android.minapi = 21
android.ndk_api = 21

