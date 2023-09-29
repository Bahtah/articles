from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import CategoryListSerializer, ArticleListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Category, Article
from users.permissions import IsOwnerOrReadOnly, MyCustomPermission


"""Просмотр залогиненным пользователям"""


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAdminUser,)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


"""Разрешение промтотра залогиненным пользователям Категорию и Статьи"""


class CategoryGetUnsaligned(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (MyCustomPermission,)


class ArticleGetUnsaligned(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = (MyCustomPermission,)