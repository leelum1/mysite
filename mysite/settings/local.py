from .base import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

#Debug toolbar
INTERNAL_IPS = ('127.0.0.1', 'localhost',)
MIDDLEWARE += (
   'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = [
   'debug_toolbar.panels.versions.VersionsPanel',
   'debug_toolbar.panels.timer.TimerPanel',
   'debug_toolbar.panels.settings.SettingsPanel',
   'debug_toolbar.panels.headers.HeadersPanel',
   'debug_toolbar.panels.request.RequestPanel',
   'debug_toolbar.panels.sql.SQLPanel',
   'debug_toolbar.panels.staticfiles.StaticFilesPanel',
   'debug_toolbar.panels.templates.TemplatesPanel',
   'debug_toolbar.panels.cache.CachePanel',
   'debug_toolbar.panels.signals.SignalsPanel',
   'debug_toolbar.panels.logging.LoggingPanel',
   'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
   'INTERCEPT_REDIRECTS': False,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static_root'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')