from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path("simulation/", views.GetTweetsSimulationAPIView.as_view(), name="get tables and send email"),
    path("", views.GetTweetsAPIView.as_view(), name="get tables and send email"),
]