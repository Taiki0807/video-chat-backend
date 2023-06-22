from django.urls import path

from .views import (
    AccountRegister,
    GetAccountInfo,
    GetAccountStatus,
    TokenDeleteView,
    TokenObtainView,
    TokenRefreshView,
    refresh_get,
)

urlpatterns = [
    path("register/", AccountRegister.as_view()),
    path("get/", GetAccountInfo.as_view()),
    path("login/", TokenObtainView.as_view()),
    path("logout/", TokenDeleteView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("status/", GetAccountStatus.as_view()),
    path("refresh-token/", refresh_get),
]
