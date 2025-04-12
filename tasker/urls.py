from django.urls import path

from tasker.views import index

app_name = "tasker"


urlpatterns = [
    path("", index, name="index"),
    ]