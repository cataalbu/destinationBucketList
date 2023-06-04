from django.http import HttpRequest
from django.test import TestCase, RequestFactory

from destination.mvc.models.Destination import Destination
from destination.mvc.models.User import GeneralUser
from destination.mvc.view.PublicDestinationListView import PublicDestinationsListView


class GetPublicDestinationsViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create test data
        destination1 = Destination.objects.create(geolocation="geolocation", title="title", image="image",
                                                  description="description", arrival_date=None, departure_date=None,
                                                  user_id=None, is_public=True)
        destination2 = Destination.objects.create(geolocation="geolocation", title="title", image="image",
                                                  description="description", arrival_date=None, departure_date=None,
                                                  user_id=None, is_public=False)
        user = GeneralUser.objects.create(username="username", password="password", isAdmin=False)

    def test_url_exists(self):
        response = self.client.post('/login/', {'username': 'username', 'password': 'password'})
        # Check the status code of the login response
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/public-destinations/')
        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

    def test_get_public_destinations(self):
        response_login = self.client.post('/login/', {'username': 'username', 'password': 'password'})
        response = self.client.get('/public-destinations/')
        destinations = response.context['destinations']
        self.assertEqual(destinations.count(), 1)
        destination = Destination.objects.create(geolocation="geolocation", title="title", image="image",
                                              description="description", arrival_date=None, departure_date=None,
                                              user_id=None, is_public=True)
        response = self.client.get('/public-destinations/')
        destinations = response.context['destinations']
        self.assertEqual(destinations.count(), 2)

    def test_get_private_destinations(self):
        response_login = self.client.post('/login/', {'username': 'username', 'password': 'password'})
        response = self.client.get('/private-destinations/')
        destinations = response.context['destinations']
        self.assertEqual(destinations.count(), 0)

        destination = Destination.objects.create(geolocation="geolocation", title="title", image="image",
                                                 description="description", arrival_date=None, departure_date=None,
                                                 user_id=1, is_public=True)
        response = self.client.get('/private-destinations/')
        destinations = response.context['destinations']
        self.assertEqual(destinations.count(), 1)

        destination = Destination.objects.create(geolocation="geolocation", title="title", image="image",
                                                 description="description", arrival_date=None, departure_date=None,
                                                 user_id=1, is_public=False)
        response = self.client.get('/private-destinations/')
        destinations = response.context['destinations']
        self.assertEqual(destinations.count(), 2)
