import json
from pstats import Stats

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Covid
from .serializer import CovidSerializer

class CovidTestViewTestCase(APITestCase):
    list_url = reverse("data-list")
    def setUp(self) :
        self.user = User.objects.create(username="test",password="some-very-strong-psw")
        self.token = Token.objects.create(user = self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)
    
    def test_covid_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response =  self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_covid_detail_retrive(self):
        response = self.client.get(reverse("data-detail",kwargs={"pk":1}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["user"],"test")