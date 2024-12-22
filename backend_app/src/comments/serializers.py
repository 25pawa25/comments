from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_dt', 'author_name', 'parent', 'is_deleted', 'children']

    def get_children(self, obj):
        children = Comment.objects.filter(parent=obj, is_deleted=False)
        return CommentSerializer(children, many=True).data
