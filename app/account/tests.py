from django.test import TestCase
from account import schema
from django.contrib.auth.models import User
from graphene_django.utils.testing import GraphQLTestCase

class UsersAPITestCase(GraphQLTestCase):
    GRAPHENE_SCHEMA = schema

    def test_query_all_users(self):
        response = self.query('''
            query {
                users {
                    id
                    username
                    email
                }
            }
        ''', content_type='application/json', accept='application/json')  # Accept başlığını da ekleyin

        self.assertResponseNoErrors(response)
        self.assertEqual(len(response.json()['data']['users']), User.objects.count())
