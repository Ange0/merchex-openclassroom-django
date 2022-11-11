from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bands/add/', views.bands_create, name="bands-create"),
    path('bands/<int:id>/update', views.bands_change, name="bands-change"),
    path('bands/<int:id>/delete', views.bands_delete, name="bands-delete"),
    path('', views.bands, name="bands"),
    path('bands/<int:id>/', views.bands_detail, name="bands-detail"),
    path('about-us/', views.about, name="about"),
    path('listings/add/', views.listings_create, name="listings-create"),
    path('listings/<int:id>/change', views.listings_change, name="listings-change"),
    path('listings/', views.listings, name="listings"),
    path('listings/<int:id>', views.listings_detail, name="listings-detail"),
    path('contact/', views.contact, name="contact"),
    path('email-sent/', views.email_sent, name="email-sent")
]
