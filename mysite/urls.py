"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('cookies/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('legal/', views.LegalTemplateView.as_view(), name='legal'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('Trinidad-Hiking/', views.HikingTemplateView.as_view(), name='hiking'),
    path('Trinidad-Tobago-Watersheds/', views.WatershedMapTemplateView.as_view(), name='watersheds'),
    path('blog/', include('blog_app.urls')),
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
