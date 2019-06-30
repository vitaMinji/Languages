from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languges',views.LanguageView)
router.register('paradigms',views.ParadigmView)
router.register('programmers',views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]
