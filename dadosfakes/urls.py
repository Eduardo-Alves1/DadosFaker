from django.urls import path
from .views import FakeDataAPIView, DadosProntosGet

urlpatterns = [
    path("generate/", FakeDataAPIView.as_view(), name="generate-fake-data"),
    path("dados-prontos/", DadosProntosGet.as_view(), name="dados-prontos"),
]
