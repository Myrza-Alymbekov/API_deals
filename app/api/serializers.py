from rest_framework import serializers
from .models import Bookmark, Collection


class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        exclude = ('user',)
        read_only_fields = ['title', 'description', 'type', 'preview_image', 'user']


class CollectionSerializer(serializers.ModelSerializer):
    bookmarks = serializers.PrimaryKeyRelatedField(queryset=Bookmark.objects.all(), many=True)

    class Meta:
        model = Collection
        exclude = ('user',)
