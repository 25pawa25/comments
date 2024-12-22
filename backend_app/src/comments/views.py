from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False).prefetch_related("children")
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_deleted = True
            instance.save()
            return Response({"status": "success", "message": "Комментарий удалён."})
        except Comment.DoesNotExist:
            return Response({"status": "error", "message": "Комментарий не найден."}, status=404)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(
                {"status": "success", "message": "Комментарий добавлен.", "comment": CommentSerializer(comment).data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

