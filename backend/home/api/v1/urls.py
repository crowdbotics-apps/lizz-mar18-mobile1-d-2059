from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomModel345pmViewSet,
    CustomModel344pmViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("custommodel344pm", CustomModel344pmViewSet)
router.register("custommodel345pm", CustomModel345pmViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
