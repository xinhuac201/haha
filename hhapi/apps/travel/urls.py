from django.urls import path,  include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('category_banner', views.CategoryBannerViewSet, basename=False)
router.register("travel_route",views.TravelRouteDescViewSet,basename=False)
router.register("travel_short_route",views.TravelShortRouteDescViewSet,basename=False)

urlpatterns = [
    path('', include(router.urls)),

]
