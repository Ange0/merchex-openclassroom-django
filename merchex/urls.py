from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('hello/', views.hello),
    path('about-us/', views.about),
    path('listing/', views.listing),
    path('contact/', views.contact)
]
