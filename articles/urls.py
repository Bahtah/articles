from rest_framework.routers import DefaultRouter
from .api import CategoryViewSet, ArticleViewSet, CategoryGetUnsaligned, ArticleGetUnsaligned

router = DefaultRouter()
router.register('category-unsaligned', CategoryGetUnsaligned, basename='category-unsaligned')
router.register('article-unsaligned', ArticleGetUnsaligned, basename='article-unsaligned')

router.register('category', CategoryViewSet, basename='category')
router.register('', ArticleViewSet, basename='article')


urlpatterns = []
urlpatterns += router.urls
