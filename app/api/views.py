from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .functions import get_page_info
from .models import Bookmark, Collection
from .permissions import IsStaffOrOwnerPermission
from .serializers import BookmarkSerializer, CollectionSerializer


class BookmarkViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    API для создания, просмотра и удаления закладок.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsStaffOrOwnerPermission]

    def perform_create(self, serializer):
        page_info = get_page_info(serializer.validated_data.get('link'))
        serializer.save(title=page_info.get('title'),
                        description=page_info.get('description'),
                        type=page_info.get('type'),
                        preview_image=page_info.get('preview_image'),
                        user=self.request.user)


class CollectionViewSet(viewsets.ModelViewSet):
    """
        API для создания, просмотра, редактирования и удаления коллекций.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsStaffOrOwnerPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
