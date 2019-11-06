from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from gluck.views import SectionListView, SectionDetailView

urlpatterns = [
     path('', views.index, name='index'),
     path('impressum', views.impressum, name='impressum'),
     path('datenschutzerklarung', views.impressum, name='datenschutzerklarung'),
     path('', SectionListView.as_view(), name='section-list'),
     path('section/<int:pk>/', SectionDetailView.as_view(), name='Section-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

