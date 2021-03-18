from faker import Factory
from rest_framework.test import APITestCase, APIClient
from accounts.models import User

faker = Factory.create()


class UserViewTest(APITestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name="test_name",
            about="test about",
            username="test_username_auth",
            email="useri@example.com",
            password="Pas$w0rd",
            phone_number="+1-202-555-0132")
        self.client = APIClient()
        self.client.force_authenticate(test_user)

    def test_should_show_user_deteil(self):
        url = self._create_get_id()
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['username'], 'test_username')

    def test_should_create_user(self):
        url = '/myuser/'
        data = {
            "first_name": "test_create_name",
            "about": "test about",
            "username": "test_create_name",
            "email": "user_create@example.com",
            "password": "Pas$w0rd",
            "phone_number": "+1-202-555-0132"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        id = str(response.data['id'])
        url = '/myuser/' + id + '/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.data['first_name'], 'test_create_name')

    def test_should_delete_user(self):
        test_user = User.objects.create_user(
            first_name="test_admin",
            about="test about",
            username="test_username_auth_admin",
            email="user_admin@example.com",
            password="Pas$w0rd",
            phone_number="+1-202-555-0133",
            is_staff=True)
        self.client.force_authenticate(test_user)
        url = self._create_get_id()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

    def _create_get_id(self):
        url = '/myuser/'
        data = {
            "first_name": "test_name",
            "about": "test about",
            "username": "test_username",
            "email": "user_create@example.com",
            "password": "Pas$w0rd",
            "phone_number": "+1-202-555-0132"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        id = str(response.data['id'])
        return '/myuser/'+id+'/'
