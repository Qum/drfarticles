from rest_framework import routers
from accounts.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'myuser', UserViewSet)

urlpatterns = router.urls