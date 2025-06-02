from rest_framework.response import Response
from rest_framework import generics
from .serializers import FakeDataRequestSerializer
from .faker_generator import generate_fake_data, generate_fake_profile


class FakeDataAPIView(generics.GenericAPIView):
    serializer_class = FakeDataRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        fields = serializer.validated_data["fields"]
        quantity = serializer.validated_data["quantity"]

        data = generate_fake_data(fields, quantity)
        return Response(data)


class DadosProntosGet(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        data = [generate_fake_profile() for _ in range(1)]
        return Response(data)
