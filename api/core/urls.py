from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirportViewSet
from .views import AirlineViewSet
from .views import RunwayViewSet
from .views import FlightViewSet

router = DefaultRouter()
router.register(r'airport', AirportViewSet, basename = 'airport')
router.register(r'airline', AirlineViewSet, basename = 'airline')
router.register(r'runway', RunwayViewSet, basename = 'runway')
router.register(r'flight', FlightViewSet, basename = 'flight')

urlpatterns = {
    path('', include(router.urls)),
}

