import graphene
from graphene_django.types import DjangoObjectType
from account.views import BreweryListView  # Örnek olarak bu şekilde dahil edin
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        #fields = ("id", "username", "email")


# class BreweryType(graphene.ObjectType):
#     id = graphene.String()
#     name = graphene.String()
#     brewery_type = graphene.String()
#     address_1 = graphene.String()
#     address_2 = graphene.String()
#     address_3 = graphene.String()
#     city = graphene.String()
#     state_province = graphene.String()
#     postal_code = graphene.String()
#     country = graphene.String()
#     longitude = graphene.String()
#     latitude = graphene.String()
#     phone = graphene.String()
#     website_url = graphene.String()
#     state = graphene.String()
#     street = graphene.String()
#     # Diğer alanları ekleyin


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    # breweries = graphene.List(BreweryType, query=graphene.String())

    # def resolve_breweries(root, info, query=None):
    #     view = BreweryListView()
    #     request = info.context
    #     response = view.get(request)
    #     return response.data

    def resolve_mymodels(self, info, **kwargs):
        return User.objects.all()

schema = graphene.Schema(query=Query)



# query {
#   breweries {
#     id
#     name
#     breweryType
#     address_1
#     address_2
#     address_3
#     city
#     state_province
#     postal_code
#     country
#     longitude
#     latitude
#     phone
#     website_url
#     state
#     street
#   }
# }

{
  "query" : {
    "id": "String",
    "name": "String",
    "breweryType": "String",
    "address1": "String",
    "address2": "String",
    "address3": "String",
    "city": "String",
    "stateProvince": "String",
    "postalCode": "String",
    "country": "String",
    "longitude": "String",
    "latitude": "String",
    "phone": "String",
    "websiteUrl": "String",
    "state": "String",
    "street": "String"
  }
  }
