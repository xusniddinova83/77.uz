from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pet.views import PetViewSet
from user.views import UserViewSet
from store.views import StoreViewSet
from address.views import AddressViewSet
from tag.views import TagViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'pet', PetViewSet)
router.register(r'user', UserViewSet)
router.register(r'store', StoreViewSet)
router.register(r'address', AddressViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="CRUD va registratsiya API'lari",
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]




