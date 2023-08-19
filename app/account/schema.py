import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
import requests

class BreweryType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    brewery_type = graphene.String()
    address_1 = graphene.String()
    address_2 = graphene.String()
    address_3 = graphene.String()
    city = graphene.String()
    state_province = graphene.String()
    postal_code = graphene.String()
    country = graphene.String()
    longitude = graphene.String()
    latitude = graphene.String()
    phone = graphene.String()
    website_url = graphene.String()
    state = graphene.String()
    street = graphene.String()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    breweries = graphene.List(BreweryType, query=graphene.String())
    def resolve_users(self, info):
        return User.objects.all()

    def resolve_breweries(self, info, query=None):
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
                    # Diğer alanları da burada ekleyin
                )
                breweries.append(brewery)

            return breweries
        except requests.exceptions.RequestException as e:
            return []
        
schema = graphene.Schema(query=Query)
