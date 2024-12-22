from django.urls import path

from comments.views import CommentViewSet

urlpatterns = [
    path('all-comments/<int:pk>/', CommentViewSet.as_view({'delete': 'destroy'})),
    path('all-comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
]