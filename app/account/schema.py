import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
import requests

# Define the GraphQL type for a brewery


class BreweryType(graphene.ObjectType):
    id = graphene.String(description="ID of the brewery")
    name = graphene.String(description="Name of the brewery")
    brewery_type = graphene.String(description="Type of the brewery")
    address_1 = graphene.String(description="Address line 1")
    address_2 = graphene.String(description="Address line 2")
    address_3 = graphene.String(description="Address line 3")
    city = graphene.String(description="City of the brewery")
    state_province = graphene.String(description="State or province")
    postal_code = graphene.String(description="Postal code")
    country = graphene.String(description="Country of the brewery")
    longitude = graphene.String(description="Longitude coordinates")
    latitude = graphene.String(description="Latitude coordinates")
    phone = graphene.String(description="Phone number")
    website_url = graphene.String(description="Website URL")
    state = graphene.String(description="State")
    street = graphene.String(description="Street name")

# Define the GraphQL type for a Django User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    # Retrieve all users
    users = graphene.List(UserType)

    # Retrieve breweries with optional query parameter
    breweries = graphene.List(BreweryType, query=graphene.String())

    def resolve_users(self, info):
        """
        Resolve the 'users' query to fetch all users.
        """
        return User.objects.all()

    def resolve_breweries(self, info, query=None):
        """
        Resolve the 'breweries' query to fetch breweries from an external API.
        """
        url = 'https://api.openbrewerydb.org/v1/breweries/'

        if query:
            url += f'search?query={query}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()

            breweries = []
            for item in data:
                brewery = BreweryType(
                    id=item['id'],
                    name=item['name'],
                    brewery_type=item['brewery_type'],
                    address_1=item['address_1'],
                    address_2=item['address_2'],
                    address_3=item['address_3'],
                    city=item['city'],
                    state_province=item['state_province'],
                    postal_code=item['postal_code'],
                    country=item['country'],
                    longitude=item['longitude'],
                    latitude=item['latitude'],
                    phone=item['phone'],
                    website_url=item['website_url'],
                    state=item['state'],
                    street=item['street']
                )
                breweries.append(brewery)

            return breweries
        except requests.exceptions.RequestException as e:
            return []


# Create a GraphQL schema
schema = graphene.Schema(query=Query)
