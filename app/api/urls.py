from django.urls import path, include
from rest_framework import routers
from .views import BookmarkViewSet, CollectionViewSet

router = routers.DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
