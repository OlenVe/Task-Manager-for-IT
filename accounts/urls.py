from django.urls import path, include

from accounts.views import SignUpView, ActivateAccountView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),

]