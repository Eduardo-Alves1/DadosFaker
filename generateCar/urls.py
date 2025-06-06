from django.urls import path
from .views import GenerateCarView


urlpatterns = [
    path("generate-car/", GenerateCarView.as_view(), name="generate-car-data"),
]
