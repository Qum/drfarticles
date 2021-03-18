from rest_framework import routers
from comments.views import CommentViewSet

router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet, basename='comments_view_set')

urlpatterns = router.urls