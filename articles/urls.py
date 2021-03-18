from rest_framework import routers

from articles.views import ArticleViewSet

router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls