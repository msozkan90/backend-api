"""
Views for the user API.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import OpenApiParameter, extend_schema
from account.consts import brewery_example  # Make sure you have this import


class UserListView(generics.ListAPIView):
    """
    API view to list all users.

    Only authenticated users can access this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user.

    Only authenticated users can access this view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserCreateView(generics.CreateAPIView):
    """
    API view to create a new user.

    Anyone can access this view (no authentication required).
    """
    serializer_class = UserSerializer


class BreweryListView(APIView):
    """
    API view to list breweries from an external API.

    Only authenticated users can access this view.
    """
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
                'example': [brewery_example],
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
        """
        Retrieve a list of breweries from an external API.

        Args:
            request: HTTP request object.

        Returns:
            Response: JSON response containing brewery data.
        """
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
