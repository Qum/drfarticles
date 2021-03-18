from faker import Factory
from rest_framework.test import APITestCase, APIClient
from accounts.models import User
from articles.models import Article

faker = Factory.create()


class CheckCommentViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        test_user = User.objects.create_user(
            first_name="test_name",
            about="test about",
            username="test_username",
            email="user@example.com",
            password="Pas$w0rd")
        self.client = APIClient()
        self.client.force_authenticate(test_user)
        Article.objects.create(author_id=1, title='title article', body='test body article')

    def test_should_show_comment_deteil(self):
        url = self._create_get_id()
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['body'], 'test body comment')

    def test_should_create_comment(self):
        url = '/comments/'
        data = {"target_article": 1, "body": "test body"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['body'], 'test body')

    def test_should_delete_comment(self):
        url = self._create_get_id()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

    def _create_get_id(self):
        url_to_create = '/comments/'
        data = {"target_article": 1, "body": "test body comment"}
        response = self.client.post(url_to_create, data, format='json')
        id = str(response.data['id'])
        return '/comments/'+id+'/'
