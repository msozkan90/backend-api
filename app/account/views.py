"""
Views for the user API.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema_view,
    extend_schema,
    OpenApiTypes,
)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class BreweryListView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='query',
                description='Query parameter for filtering breweries.',
                type=str,
                required=False,
            ),
        ],
        responses={
            status.HTTP_200_OK: {
                'description': 'Brewery data',
                'example': [
                       {
                        "id": "5128df48-79fc-4f0f-8b52-d06be54d0cec",
                        "name": "(405) Brewing Co",
                        "brewery_type": "micro",
                        "address_1": "1716 Topeka St",
                        "address_2": None,
                        "address_3": None,
                        "city": "Norman",
                        "state_province": "Oklahoma",
                        "postal_code": "73069-8224",
                        "country": "United States",
                        "longitude": "-97.46818222",
                        "latitude": "35.25738891",
                        "phone": "4058160490",
                        "website_url": "http://www.405brewing.com",
                        "state": "Oklahoma",
                        "street": "1716 Topeka St"
                    },
                    # Add more example objects if needed
                ],
            },
            status.HTTP_500_INTERNAL_SERVER_ERROR: {
                'description': 'An error occurred while fetching data.',
                'example': {
                    'error': 'An error occurred while fetching data.'
                }
            }
        }
    )
    def get(self, request, *args, **kwargs):
        url = 'https://api.openbrewerydb.org/v1/breweries/'

        query_param = request.query_params.get('query', None)
        if query_param:
            url += f'search?query={query_param}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()

            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'An error occurred while fetching data.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)