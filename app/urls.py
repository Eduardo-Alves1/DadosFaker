from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/dadosfakes/", include("dadosfakes.urls")),
    path("api/veiculos/", include("generateCar.urls")),
]
