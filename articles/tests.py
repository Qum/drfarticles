from faker import Factory
from rest_framework.test import APITestCase, APIClient
from accounts.models import User

faker = Factory.create()


class ArticleViewTest(APITestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name="test_name",
            about="test about",
            username="test_username",
            email="user@example.com",
            password="Pas$w0rd",
            phone_number="+1-202-555-0132")
        self.client = APIClient()
        self.client.force_authenticate(test_user)

    def test_should_show_article_deteil(self):
        url = self._create_get_id()
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['body'], 'test body article')

    def test_should_create_article(self):
        url = '/articles/'
        data = {"title": 'test title', "body": "create test body"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['body'], 'create test body')

    def test_should_delete_article(self):
        url = self._create_get_id()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

    def _create_get_id(self):
        url_to_create = '/articles/'
        data = {'title': 'title article', "body": "test body article"}
        response = self.client.post(url_to_create, data, format='json')
        id = str(response.data['id'])
        return '/articles/'+id+'/'
